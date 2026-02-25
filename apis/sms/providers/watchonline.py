# Github : https://github.com/Bllare
from apis.sms.abstract import AbstractSmsProvider
from apis.status import SendStatus
import requests

class SmsWatchonline(AbstractSmsProvider):
    name = "SMS Watchonline"
    
    def send_request(self, phone: str) -> SendStatus:
        
        headers = self.get_headers()
        payload = {"mobile":phone}

        session = requests.Session()

        r = session.get("https://api.watchonline.shop/api/v1/init")
        
        token = r.json()["data"]["token"]
        headers["Authorization"] = f"Bearer {token}"

        return session.post("https://api.watchonline.shop/api/v1/otp/request", json=payload, headers=headers,timeout=10)
