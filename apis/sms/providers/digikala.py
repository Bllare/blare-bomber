# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class SmsDigikala(PostRequestSmsProvider):
    name = "SMS Digikala"
    url = "https://api.digikala.com/v1/user/authenticate/"
    payload_type = "json"


    def get_payload(self, phone: str) -> dict:
        return {"username": phone}
    
