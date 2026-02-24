# Github : https://github.com/Bllare

from apis.sms.base import SmsProvider


class SmsTap33(SmsProvider):
    name = "SMS Tap33"
    url = "https://tap33.me/api/v2/user"
    method = "POST" 
    payload_type = "json"

    def get_payload(self, phone):
        return {"credential": {"phoneNumber": phone, "role": "PASSENGER"}}

