# Github : https://github.com/Bllare

from apis.sms.base import PostRequestSmsProvider


class SmsTap33(PostRequestSmsProvider):
    name = "SMS Tap33"
    url = "https://tap33.me/api/v2/user"
    payload_type = "json"

    def get_payload(self, phone):
        return {"credential": {"phoneNumber": phone, "role": "PASSENGER"}}

