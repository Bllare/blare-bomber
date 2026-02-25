# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class Ninishopi(PostRequestSmsProvider):
    name = "SMS Ninishopi"
    url = "https://ninishopi.com/wp-admin/admin-ajax.php"
    payload_type = "data"

    def get_payload(self, phone):
        return  {
        "action": "login_register_together",
        "value": phone,
        "captcha": "false",
        "nonce": "9d69b8fc24"
    }
    