# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider


class SmsDigikalajet(PostRequestSmsProvider):
    name = "SMS Digikalajet"
    url = "https://api.digikalajet.ir/user/login-register/"
    payload_type = "json"

    def get_payload(self, phone):
        return {"phone": phone}
