from apis.sms.base import SmsProvider

class SmsDigikala(SmsProvider):
    name = "SMS Digikala"
    url = "https://api.digikala.com/v1/user/authenticate/"
    method = "POST"
    payload_type = "json"


    def get_payload(self, phone: str) -> dict:
        return {"username": phone}
    
