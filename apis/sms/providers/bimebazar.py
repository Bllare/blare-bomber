# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class SmsBimebazar(PostRequestSmsProvider):
    name = "SMS Bimebazar"
    url = "https://bimebazar.com/accounts/api/login_sec/"
    payload_type = "json"

    def get_payload(self, phone: str) -> dict:
        return {"username": phone}

