# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Sazkala(SmsProvider):
    name = "SMS Sazkala"
    url = "https://sazkala.com/new-register-login/"
    method = "POST"
    payload_type = "data"

    def get_payload(self, phone):
        return {
        "custom_auth_nonce": "f5edcd13b0",
        "_wp_http_referer": "/new-register-login/",
        "emailverified": "",
        "emailnotverified": "",
        "numnotverified": "",
        "current-step": "start",
        "prev-step": "",
        "user_login": phone
    }
    