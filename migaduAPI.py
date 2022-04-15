import requests

import config

class MigaduAPI():
    
    def __init__(self) -> None:
        self._redirect_emails = {
            e.split("@")[1]: e for e in config.SPAM_MAILS
        }
        self._domains = [e.split("@")[1] for e in config.SPAM_MAILS]
        self._url = config.MIGADU_URL

        self._admin_account = config.ADMIN_ACCOUNT
        self._api_token = config.API_TOKEN


    def create_alias(self, name:str, domain:str) -> str:
        """
        Field 	    Type 	Note
        local_part 	String 	Read Only
        domain 	    String 	Read Only
        address 	String 	Read Only
        destinations 	Array or CSV String 	
        """
        endpoint = f"{self._url}/domains/{domain}/aliases"
        data = {
            "local_part": name,
            "destinations": self._redirect_emails[domain]
        }

        req = requests.post(endpoint, data=data, auth=(self._admin_account, self._api_token))

        if req.ok:
            return req.text
        else:
            raise APIException(f"Coudn't finish API-Call: [{req.status_code}]{req.text}")

    def delete_alias(self, name:str, domain:str) -> str:
        endpoint = f"{self._url}/domains/{domain}/aliases/{name}"
        req = requests.delete(endpoint, auth=(self._admin_account, self._api_token))

        if req.ok:
            return req.text
        else:
            raise APIException(f"Coudn't finish API-Call: [{req.status_code}]{req.text}")
    
    def get_domains(self) -> list:
        return self._domains


class APIException(BaseException):
    pass

if __name__ == "__main__":
    mapi = MigaduAPI()
    #out = mapi.create_alias("spammerino")
    out = mapi.delete_alias("spammerino")
    print(out)