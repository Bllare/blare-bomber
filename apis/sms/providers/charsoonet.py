from apis.status import SendStatus
from apis.sms.base import PostRequestSmsProvider
import string
import random

class SmsCharsoonet(PostRequestSmsProvider):
    name = "SMS Charsoonet"
    url = "https://charsoonet.com/login"
    payload_type = "data"


    def random_text_generator(self, lenth = 10):
        return ''.join(random.choices(string.ascii_letters, k=lenth))
    
    def get_headers(self):
        headers = super().get_headers()
        headers.update({
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest"
        })
        return headers

    def get_payload(self, phone: str) -> dict:
        return {
            "id_customer": "",
            "back": "",
            "firstname": self.random_text_generator(),
            "lastname": self.random_text_generator(),
            "email": f"{self.random_text_generator(),}@gmail.com",
            "password": self.random_text_generator(),
            "action": "register",
            "username": phone,
            "ajax": "1"
        }

    def handle_response(self, response):
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("result"):
                    return SendStatus.SENT
            except:
                pass
        return super().handle_response(response)