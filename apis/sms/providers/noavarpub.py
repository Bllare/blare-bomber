from apis.sms.base import SmsProvider


class SmsNoavarpub(SmsProvider):
    name = "SMS Noavarpub"
    url = "https://noavarpub.com/logins/login.php"
    method = "POST"
    payload_type = "data"

    def get_payload(self, phone: str) -> dict:
        return {"phone": phone, "submit": "123"}