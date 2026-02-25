# Github: https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider


class SmsNeshatrokh(PostRequestSmsProvider):
    name = "SMS Neshatrokh"
    url = "https://api.neshatrokh.com/api/v1/user/login/"
    payload_type = "json"

    def get_payload(self, phone: str) -> dict:
        return {"phone_number": phone}