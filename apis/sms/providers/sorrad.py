# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class Sorrad(PostRequestSmsProvider):
    name = "SMS Sorrad"
    url = "https://sorrad.ir/api/v1/sessions/login_request"
    payload_type = "json"

    def get_payload(self, phone):
        return {"mobile_phone": phone}
    