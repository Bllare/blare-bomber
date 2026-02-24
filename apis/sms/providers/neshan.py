# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
import uuid

class SmsNeshan(SmsProvider):
    name = "SMS Neshan"
    url = "https://neshan.org/maps/pwa-api/login/sms/request?mobileNumber={phone}&uuid=web_{uuid}"


    def send(self, phone: str) -> SendStatus:
        try:
            headers = self.get_headers()
            uid  = uuid.uuid1()
            
            response = requests.get(self.url.format(phone=phone, uuid=uid), headers=headers)
            
            return self.handle_response(response)
        except:
            return SendStatus.ERROR