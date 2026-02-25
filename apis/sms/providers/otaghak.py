# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class SmsOtaghak(PostRequestSmsProvider):
    name = "SMS Otaghak"
    url = "https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode"
    payload_type = "json"

    def get_payload(self, phone):
        return {"userName": phone}
    