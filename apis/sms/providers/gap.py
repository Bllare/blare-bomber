# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider


class SmsGap(SmsProvider):
    name = "SMS Gap"
    url = "https://core.gap.im/v1/user/add.json"
    method = "POST"
    payload_type = "params"


    def get_payload(self, phone: str) -> dict:
        return {"mobile": phone}

