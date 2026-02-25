# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider
from apis.status import SendStatus

class Taghche(PostRequestSmsProvider):
    name = "SMS Taghche"
    url = "https://gw.taaghche.com/v4/site/auth/login"
    payload_type = "json"

    def get_payload(self, phone):
        return  {"contact":phone,"forceOtp":"false"}
    
    def handle_response(self, response):
        """Default response handler, can be overridden by subclass if needed"""
        if "ارسال شد" in response.json()['message']:
            return SendStatus.SENT
        return SendStatus.UNKNOWN

    