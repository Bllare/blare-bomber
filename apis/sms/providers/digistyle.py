from apis.sms.base import SmsProvider


class SmsDigistyle(SmsProvider):
    name = "SMS Digistyle"
    url = "https://www.digistyle.com/users/login-register/"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone: str) -> dict:
        return {"loginRegister[email_phone]": phone}

