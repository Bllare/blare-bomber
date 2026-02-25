# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider
import uuid

class SmsMydigipay(PostRequestSmsProvider):
    name = "SMS Mydigipay"
    url = "https://app.mydigipay.com/digipay/api/users/send-sms" 
    payload_type = "json" 

    def get_payload(self, phone):
        return {"cellNumber": phone,"device": {"deviceId": str(uuid.uuid4()),"deviceModel": "WEB_BROWSER","deviceAPI": "WEB_BROWSER","osName": "WEB"}}
