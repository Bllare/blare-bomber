# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class SmsAlibaba(SmsProvider):
    name = "SMS Alibaba"
    url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone: str) -> dict:
        return {"phoneNumber": phone}

