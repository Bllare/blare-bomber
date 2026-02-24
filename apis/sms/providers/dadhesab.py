from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests

class SmsDadhesab(SmsProvider):
    name = "SMS Dadhesab"
    url = "https://api.dadhesab.ir/user/login"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = self.get_headers()
            
            # Pass that local variable to payload logic
            payload = {
                "username": phone,
                "deviceInfo": {"userAgent": headers["User-Agent"]}, # Now it works
                "appVersion": "10.4.5",
                "appFlavor": "webapp"
            }

            response = requests.post(self.url, json=payload, headers=headers, timeout=10)
            
            return self.handle_response(response)
        
        except Exception:
            return SendStatus.ERROR
        
    def get_payload(self, phone):
        return {}

