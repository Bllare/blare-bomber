# Github: https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider


class SmsElanza(PostRequestSmsProvider):
    name = "SMS Elanza"
    url = "https://api.elanza.com/auth/request"
    payload_type = "json"

    def get_payload(self, phone: str) -> dict:
        return {"contact": phone}