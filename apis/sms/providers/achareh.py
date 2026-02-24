# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class SmsAchareh(SmsProvider):
    name = "SMS Achareh"
    url = "https://api.achareh.co/v2/accounts/login/" 
    method = "POST"
    payload_type = "json"
    

    def get_payload(self, phone: str) -> dict:
        return {"phone": f"98{int(phone)}"}
    
