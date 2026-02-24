# Github : https://github.com/Bllare

from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests


class SmsTorob(SmsProvider):
    name = "SMS Torob"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = self.get_headers()
            params={"phone_number": phone}

            response = requests.get("https://api.torob.com/a/phone/send-pin/", headers=headers,params=params)

            return self.handle_response(response)
        except:
            return SendStatus.ERROR