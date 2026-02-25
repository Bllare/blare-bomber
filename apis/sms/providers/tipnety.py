# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Tipnety(SmsProvider):
    name = "SMS Tipnety"
    url = "https://tipnety.com/api/v1/auth/otp/send"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return  {
        "mobile": phone,
        "type": "login"
    }
    