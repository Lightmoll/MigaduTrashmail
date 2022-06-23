# Migadu Trash Mail Generator [MTMG]
Selfhosted Trashmail Generator for E-Mail addresses hosted on [migadu.com](https://midadu.com).

<p align="middle">
  <img src="https://i.imgur.com/qwh2giC.png" width="32%" />
  <img src="https://i.imgur.com/wk7OIZ9.png" width="32%" /> 
  <img src="https://i.imgur.com/1XMZ7nC.png" width="32%" />
</p>


## Features:
 - modern UI
 - adaptive darkmode
 - all-in-one solution
 - very lightweight
 - completely self hosted

## How it works
The e-mail generator will create an alias with the specified name, which will redirect to the specified e-mail inbox in `config.py::SPAM_MAILS`. Then after the spam-alias is not in use, the program will simply delete the alias and all emails send to the old alias will be rejected. However, if at a later point in time the same "fake" e-mail is required a new alias may be created and redirecting continues.

_Note_: Because of migadu limitations you can only create an alias for the same domain. Therefore all emails generated with one domain, will redirect to the correspronding e-mail inbox listed.

## Installation (Testing)
1. install python3 and pip on your local system
2. (optional) create a new venv
3. install all requirements by `pip3 install -r requirements.txt`
4. Copy default_config.py to config.py and edit it
5. run application with `python3 server.py`
6. you can access the webpage on 

## Installation (Production)
1. follow steps 1-3 in testing build
2. install `gunicorn3`
3. run the server with `gunicorn server:app -w 2`
    where 2 corresponds with the number of workers spawned for the app
4. configure your reverse proxy to redirect all traffic to port 8000

## HTTP / HTTPS
Since there are no passwords transmitted over the actual webpage (all API calls are done securely via the backend), a HTTPS connection is not strictly neccessary. 

However copying to clipboard won't be possible without HTTPS. This only works from trusted sources e.g. a connection over HTTPS.

## Beta Notice
The software is currently in beta, some aspects may not yet work as intedend, or at all. Please be patient until I release the full version.