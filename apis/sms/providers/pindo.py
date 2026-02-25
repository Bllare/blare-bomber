# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class SmsPindo(PostRequestSmsProvider):
    name = "SMS Pindo"
    url = "https://api.pindo.ir/v1/user/login-register/"
    payload_type = "json"

    def get_payload(self, phone):
        return {"phone": phone}

