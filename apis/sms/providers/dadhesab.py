# Github : https://github.com/Bllare
from apis.sms.abstract import AbstractSmsProvider
from apis.status import SendStatus
import requests

class SmsDadhesab(AbstractSmsProvider):
    name = "SMS Dadhesab"
    url = "https://api.dadhesab.ir/user/login"

    def send_request(self, phone: str) -> SendStatus:
  
        headers = self.get_headers()
        
        # Pass that local variable to payload logic
        payload = {
            "username": phone,
            "deviceInfo": {"userAgent": headers["User-Agent"]}, # Now it works
            "appVersion": "10.4.5",
            "appFlavor": "webapp"
        }

        return requests.post(self.url, json=payload, headers=headers, timeout=10)
            
