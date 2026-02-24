# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class SmsPindo(SmsProvider):
    name = "SMS Pindo"
    url = "https://api.pindo.ir/v1/user/login-register/"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {"phone": phone}

