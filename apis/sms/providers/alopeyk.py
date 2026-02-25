# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class SmsAlopeyk(PostRequestSmsProvider):
    name = "SMS Alopeyk"
    url = "https://api.alopeyk.com/safir-service/api/v1/login"
    payload_type = "json"
    
    def get_payload(self, phone: str) -> dict:
        return {"phone": phone}
    
