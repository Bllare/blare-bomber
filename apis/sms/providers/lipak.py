
from apis.sms.abstract import AbstractSmsProvider
from apis.status import SendStatus
import requests

class Lipak(AbstractSmsProvider):
    url = "https://lipak.com/api/v1/auth/init"

    def send_request(self, phone_number):
        headers = self.get_headers()
        headers['phone_number'] = phone_number

        return requests.get(self.url,headers=headers)


    def handle_response(self, response):
        if response.json()['ok']:
            return SendStatus.SENT
        
        return SendStatus.UNKNOWN
