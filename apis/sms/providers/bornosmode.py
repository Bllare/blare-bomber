# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class Bornosmode(PostRequestSmsProvider):
    name = "SMS Bornosmode"
    url = "https://bornosmode.com/api/loginRegister/"
    payload_type = "data"

    def get_payload(self, phone):
        return {
        "mobile": phone,
        "withOtp": "1"
    }
    