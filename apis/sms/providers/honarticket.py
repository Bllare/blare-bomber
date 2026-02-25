
from apis.sms.base import PostRequestSmsProvider
from apis.status import SendStatus
from secrets import token_hex as random_csrf

class HonarTicket(PostRequestSmsProvider):
    name = "SMS honarticket"
    url = "https://user.zirbana.com/v2/register"
    payload_type = "json"

    def get_payload(self, phone):
        return  {
        "mobile": phone,
        "client_id": "17",
        "client_secret": random_csrf(40)
    }
    
    def handle_response(self, response):
        if response.json()['ok']:
            return SendStatus.SENT
        
        return SendStatus.UNKNOWN
