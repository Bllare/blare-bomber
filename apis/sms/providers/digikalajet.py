# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider


class SmsDigikalajet(SmsProvider):
    name = "SMS Digikalajet"
    url = "https://api.digikalajet.ir/user/login-register/"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {"phone": phone}
