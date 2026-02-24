# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class SmsOtaghak(SmsProvider):
    name = "SMS Otaghak"
    url = "https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {"userName": phone}
    