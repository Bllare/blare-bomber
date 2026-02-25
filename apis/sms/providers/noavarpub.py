# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider


class SmsNoavarpub(PostRequestSmsProvider):
    name = "SMS Noavarpub"
    url = "https://noavarpub.com/logins/login.php"
    payload_type = "data"

    def get_payload(self, phone: str) -> dict:
        return {"phone": phone, "submit": "123"}