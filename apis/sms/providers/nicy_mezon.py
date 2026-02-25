# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class NicyMezon(SmsProvider):
    name = "SMS NicyMezon"
    url = "https://www.nicy-mezon.ir/users/fastlogin"
    method = "POST"
    payload_type = "data"

    def get_payload(self, phone):
        return  {
        "tel": phone
    }
    