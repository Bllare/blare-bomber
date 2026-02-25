# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Sorrad(SmsProvider):
    name = "SMS Sorrad"
    url = "https://sorrad.ir/api/v1/sessions/login_request"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {"mobile_phone": phone}
    