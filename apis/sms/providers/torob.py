# Github : https://github.com/Bllare

from apis.sms.abstract import AbstractSmsProvider
from apis.status import SendStatus
import requests


class SmsTorob(AbstractSmsProvider):
    name = "SMS Torob"

    def send_request(self, phone: str) -> SendStatus:
        headers = self.get_headers()
        params={"phone_number": phone}

        return  requests.get("https://api.torob.com/a/phone/send-pin/", headers=headers,params=params)

