# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class SmsNovinparse(PostRequestSmsProvider):
    name = "SMS Novinparse"
    url = "https://novinparse.com/Page/PageAction.aspx"
    payload_type = "data"

    def get_payload(self, phone):
        return {"Action": "SendVerifyCode","mobile": phone}
