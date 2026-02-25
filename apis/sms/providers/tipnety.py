# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class Tipnety(PostRequestSmsProvider):
    name = "SMS Tipnety"
    url = "https://tipnety.com/api/v1/auth/otp/send"
    payload_type = "json"

    def get_payload(self, phone):
        return  {
        "mobile": phone,
        "type": "login"
    }
    