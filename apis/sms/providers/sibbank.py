# Github : https://github.com/Bllare

from apis.sms.base import PostRequestSmsProvider

class SmsSibbank(PostRequestSmsProvider):
    name = "SMS Sibbank"
    url = "https://api.sibbank.ir/v1/auth/login"
    payload_type = "json"

    def get_payload(self, phone):
        return {"phone_number": phone}

