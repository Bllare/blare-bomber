# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider


class SmsGap(PostRequestSmsProvider):
    name = "SMS Gap"
    url = "https://core.gap.im/v1/user/add.json"
    payload_type = "params"


    def get_payload(self, phone: str) -> dict:
        return {"mobile": phone}

