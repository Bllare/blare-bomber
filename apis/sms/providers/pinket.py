# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class SmsPinket(PostRequestSmsProvider):
    name = "SMS Pinket"
    url = "https://pinket.com/api/cu/v2/phone-verification"
    payload_type = "json"

    def get_payload(self, phone):
        return  {"phoneNumber": phone}
