# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Riiha(SmsProvider):
    name = "SMS Riiha"
    url = "https://www.riiha.ir/api/v1.0/authenticate"
    method = "POST"
    payload_type = "data"

    def get_payload(self, phone):
        return {
        "mobile": phone,
        "mobile_code": "",
        "type": "mobile"
    }
    