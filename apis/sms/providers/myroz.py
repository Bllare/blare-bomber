# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class SmsMyroz(SmsProvider):
    name = "SMS Myroz"
    url = "https://myroz.ir/wp-admin/admin-ajax.php"
    method = "POST"
    payload_type = "data"

    def get_payload(self, phone):
        return {"action": "stm_login_register","type": "mobile","input": phone}

