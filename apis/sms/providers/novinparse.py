# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class SmsNovinparse(SmsProvider):
    name = "SMS Novinparse"
    url = "https://novinparse.com/Page/PageAction.aspx"
    method = "POST"
    payload_type = "data"

    def get_payload(self, phone):
        return {"Action": "SendVerifyCode","mobile": phone}
