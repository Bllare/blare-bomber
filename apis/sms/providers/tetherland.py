# Github : https://github.com/Bllare

from apis.sms.base import PostRequestSmsProvider


class SmsTetherland(PostRequestSmsProvider):
    name = "SMS Tetherland"
    url = "https://service.tetherland.com/api/v5/login-register"
    payload_type = "json"

    def get_payload(self, phone):
        return {"phone": phone}
