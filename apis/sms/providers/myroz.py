# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class SmsMyroz(PostRequestSmsProvider):
    name = "SMS Myroz"
    url = "https://myroz.ir/wp-admin/admin-ajax.php"
    payload_type = "data"

    def get_payload(self, phone):
        return {"action": "stm_login_register","type": "mobile","input": phone}

