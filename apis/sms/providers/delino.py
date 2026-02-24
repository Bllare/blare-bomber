# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider


class SmsDelino(SmsProvider):
    name = "SMS Delino"
    url = "https://www.delino.com/user/register"
    method = "POST"
    payload_type = "data"

    def get_headers(self):
        headers = super().get_headers()
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        return headers
    
    def get_payload(self, phone: str) -> dict:
        return f"mobile={phone}"

