from apis.sms.base import SmsProvider

class SmsBimebazar(SmsProvider):
    name = "SMS Bimebazar"
    url = "https://bimebazar.com/accounts/api/login_sec/"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone: str) -> dict:
        return {"username": phone}

