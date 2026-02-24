from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests

class SmsWatchonline(SmsProvider):
    name = "SMS Watchonline"
    url = "https://api.watchonline.shop/api/v1/otp/request"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = self.get_headers()
            payload = {"mobile":phone}

            session = requests.Session()

            r = session.get(self.url)
            
            token = r.json()["data"]["token"]
            headers["Authorization"] = f"Bearer {token}"

            response = session.post("https://api.watchonline.shop/api/v1/otp/request", json=payload, headers=headers,timeout=10)

            return self.handle_response(response)
        
        except:
            return SendStatus.ERROR
    
    def get_payload(self, phone):
        return {}