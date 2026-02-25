# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class NicyMezon(PostRequestSmsProvider):
    name = "SMS NicyMezon"
    url = "https://www.nicy-mezon.ir/users/fastlogin"
    payload_type = "data"

    def get_payload(self, phone):
        return  {
        "tel": phone
    }
    