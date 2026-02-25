# Github : https://github.com/Bllare
from apis.sms.abstract import AbstractSmsProvider
from apis.status import SendStatus
import requests
import uuid

class SmsNeshan(AbstractSmsProvider):
    name = "SMS Neshan"
    url = "https://neshan.org/maps/pwa-api/login/sms/request?mobileNumber={phone}&uuid=web_{uuid}"


    def send_request(self, phone: str) -> SendStatus:
        headers = self.get_headers()
        uid  = uuid.uuid1()
        
        return requests.get(self.url.format(phone=phone, uuid=uid), headers=headers)
            
