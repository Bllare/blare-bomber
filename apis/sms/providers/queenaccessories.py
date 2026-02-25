# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class SmsQueenaccessories(PostRequestSmsProvider):
    name = "SMS Queenaccessories"
    url = "https://queenaccessories.ir/api/v1/sessions/login_request"
    payload_type = "json"

    def get_payload(self, phone):
        return {"mobile_phone": phone}
