# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class Pooshakesanli(PostRequestSmsProvider):
    name = "SMS Pooshakesanli"
    url = "https://pooshakesanli.com/process-request/ajax"
    payload_type = "data"

    def get_payload(self, phone):
        return  {
        "form": "sendVerificationCode",
        "username": phone,
        "token": ""
    }
    