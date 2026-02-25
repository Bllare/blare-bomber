# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Bornosmode(SmsProvider):
    name = "SMS Bornosmode"
    url = "https://bornosmode.com/api/loginRegister/"
    method = "POST"
    payload_type = "data"

    def get_payload(self, phone):
        return {
        "mobile": phone,
        "withOtp": "1"
    }
    