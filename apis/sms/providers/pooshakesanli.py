# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Pooshakesanli(SmsProvider):
    name = "SMS Pooshakesanli"
    url = "https://pooshakesanli.com/process-request/ajax"
    method = "POST"
    payload_type = "data"

    def get_payload(self, phone):
        return  {
        "form": "sendVerificationCode",
        "username": phone,
        "token": ""
    }
    