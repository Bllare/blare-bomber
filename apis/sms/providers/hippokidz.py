# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class Hippokidz(PostRequestSmsProvider):
    name = "SMS Hippokidz"
    url = "https://hippokidz.ir/wp-admin/admin-ajax.php"
    payload_type = "data"

    def get_payload(self, phone):
        return {
        "action": "login_register_together",
        "value": phone,
        "captcha": "false",
        "nonce": "fe0217a2de"
    }
    