# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests

class SmsFilmnet(SmsProvider):
    name = "SMS Filmnet"
    url = "https://api-v2.filmnet.ir/access-token/users/{phone}/otp"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = self.get_headers()            
            response = requests.get(url=self.url.format(phone=phone),headers=headers, timeout=10)
            return self.handle_response(response)
            
        except Exception as e:
            return SendStatus.ERROR



