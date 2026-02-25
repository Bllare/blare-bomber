# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class SmsDivar(PostRequestSmsProvider):
    name = "SMS Divar"
    url = "https://api.divar.ir/v5/auth/authenticate"
    payload_type = "json"

    def get_payload(self, phone):
        return {"phone":str(int(phone))}
