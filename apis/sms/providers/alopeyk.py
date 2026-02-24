# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class SmsAlopeyk(SmsProvider):
    name = "SMS Alopeyk"
    url = "https://api.alopeyk.com/safir-service/api/v1/login"
    method = "POST"
    payload_type = "json"
    
    def get_payload(self, phone: str) -> dict:
        return {"phone": phone}
    
