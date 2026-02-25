# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Aramii(SmsProvider):
    name = "SMS Aramii"
    url = "https://aramii.ir/wp-admin/admin-ajax.php"
    method = "POST"
    payload_type = "data"

    def get_payload(self, phone):
        return  {
        "action": "send_verify_code",
        "phone": phone
    }
    