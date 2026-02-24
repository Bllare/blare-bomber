from apis.sms.base import SmsProvider


class SmsTetherland(SmsProvider):
    name = "SMS Tetherland"
    url = "https://service.tetherland.com/api/v5/login-register"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {"phone": phone}
