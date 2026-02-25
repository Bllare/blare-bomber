# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider


class SmsAdinehbook(PostRequestSmsProvider):
    name = "SMS Adinehbook"
    url = "https://www.adinehbook.com/gp/flex/sign-in.html"
    payload_type = "data"


    def get_headers(self):
        headers = super().get_headers()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        return headers

    def get_payload(self, phone: str) -> dict:
        return  f"path=&action=sign&phone_cell_or_email={phone}&login-submit=%D8%AA%D8%A7%DB%8C%DB%8C%D8%AF"

