# Github: https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider


class SmsHomehr(PostRequestSmsProvider):
    name = "SMS Homehr"
    url = "https://api.homehr.ir/api/front/auth/authUser"
    payload_type = "json"

    def get_payload(self, phone: str) -> dict:
        return {
            "number": phone,
            "type": "mobile",
            "action": "Number"
        }