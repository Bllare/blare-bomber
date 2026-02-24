from apis.sms.base import SmsProvider
import uuid

class SmsMydigipay(SmsProvider):
    name = "SMS Mydigipay"
    url = "https://app.mydigipay.com/digipay/api/users/send-sms" 
    method = "POST"
    payload_type = "json" 

    def get_payload(self, phone):
        return {"cellNumber": phone,"device": {"deviceId": str(uuid.uuid4()),"deviceModel": "WEB_BROWSER","deviceAPI": "WEB_BROWSER","osName": "WEB"}}
