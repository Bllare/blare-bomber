# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider


class SmsDigistyle(PostRequestSmsProvider):
    name = "SMS Digistyle"
    url = "https://www.digistyle.com/users/login-register/"
    payload_type = "json"

    def get_payload(self, phone: str) -> dict:
        return {"loginRegister[email_phone]": phone}

