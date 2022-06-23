import re
import time
import json
import random

from flask import Flask, config
from flask import redirect, render_template, request
from tinydb import TinyDB
from tinydb.queries import where

import migaduAPI
import config

db = TinyDB("aliases.db")
mapi = migaduAPI.MigaduAPI()
app = Flask(__name__)


domains = mapi.get_domains()

@app.before_request
def pre(): #TODO run on cronjob
    purge_domains()


@app.route('/')
def index():
    return render_template('index.html', reg_alias=db.all(), domains=domains)


@app.route('/api/create')
def handle_create():
    domain = request.args.get("domain")
    name = request.args.get("name")
    if name == None or domain == None:
        return redirect("/#error")

    if name == "":
        name = random.choices(config.BASE_WORDS, k=2)
        name = "".join(name)

    regex = re.compile(r"[_A-Za-z0-9\.]{2,30}") #the regex is only supposed to mitigate exploitation of the api

    if regex.fullmatch(name) == None or regex.fullmatch(domain) == None:
        return redirect("/#error")

    try:
        register_domain(name, domain)
    except migaduAPI.APIException as e:
        print(f"Exception: {e}")
        return redirect("/#error")
    return redirect("/#created")


@app.route('/api/del/<email>')
def handle_delete(email):
    name, domain = email.lower().split("@")
    if not config.DRYRUN: mapi.delete_alias(name, domain)
    db.remove(where("whole_email") == email)
    print(db.all())
    return redirect("/#deleted")


@app.route('/api/extend/<email>') #TODO add timing aswell
def handle_extend(email):
    return redirect("/#extendet")


def register_domain(name, domain, expiry_delta=15*60):
    entry = {
        "expiry": time.time() + expiry_delta,
        "name": name,
        "domain": domain,
        "whole_email": name+"@"+domain,
        "created": time.time()
    }

    if not config.DRYRUN: mapi.create_alias(name, domain) 
    db.insert(entry)


def purge_domains():
    try:
        results = db.search(where("expiry") < time.time()) #this failes every x loads
    except json.decoder.JSONDecodeError:
        print("Hit json error")
        pass #seems to be a bug of tinydb
    for result in results:
        if not config.DRYRUN: mapi.delete_alias(result["name"].lower(), result["domain"].lower())
        db.remove(doc_ids=[result.doc_id])




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
