from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests


class SmsTorob(SmsProvider):
    name = "SMS Torob"
    url  = "https://api.torob.com/a/phone/send-pin/"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = self.get_headers()
            params={"phone_number": phone}

            response = requests.get(self.url, headers=headers,params=params)

            return self.handle_response(response)
        except:
            return SendStatus.ERROR
        
    def get_payload(self, phone):
        return {}