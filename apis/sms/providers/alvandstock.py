# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class Alvandstock(PostRequestSmsProvider):
    name = "SMS Alvandstock"
    url = "https://alvandstock.com/wp-admin/admin-ajax.php"
    payload_type = "data"

    def get_payload(self, phone):
        return  {
        "action": "mreeir_send_sms",
        "mobileemail": phone,
        "userisnotauser": "",
        "type": "mobile",
        "captcha": "",
        "captchahash": "",
        "security": "31a073481f"
    }
    