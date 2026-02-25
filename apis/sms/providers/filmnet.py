# Github : https://github.com/Bllare
from apis.sms.abstract import AbstractSmsProvider
from apis.status import SendStatus
import requests

class SmsFilmnet(AbstractSmsProvider):
    name = "SMS Filmnet"
    url = "https://api-v2.filmnet.ir/access-token/users/{phone}/otp"

    def send_request(self, phone: str) -> SendStatus:        
        headers = self.get_headers()            
        return requests.get(url=self.url.format(phone=phone),headers=headers, timeout=10)




