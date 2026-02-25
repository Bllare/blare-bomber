# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Alvandstock(SmsProvider):
    name = "SMS Alvandstock"
    url = "https://alvandstock.com/wp-admin/admin-ajax.php"
    method = "POST"
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
    