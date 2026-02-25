# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Koohkade(SmsProvider):
    name = "SMS Koohkade"
    url = "https://koohkade.com/wp-admin/admin-ajax.php"
    method = "POST"
    payload_type = "data"

    def get_payload(self, phone):
        return {
        "action": "mwpl_smart_login_form_check_username",
        "nonce": "084d4722ed",
        "smart_login_username": phone,
        "password": "",
        "dynamic_code": ""
    }
    