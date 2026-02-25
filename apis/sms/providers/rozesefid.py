# Github: https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider


class SmsRozesefid(PostRequestSmsProvider):
    name = "SMS Rozesefid"
    url = "https://api.rozesefid.com/auth/login"
    payload_type = "json"

    def get_headers(self):
        headers = super().get_headers()
        # Add the custom loginKey header (seems static in the HAR)
        headers["loginKey"] = "YXNkbDtsOywvLnAsU0RMOlNBREN3MzQzNTJHUl4oKkAmIykqKClAKEYp"
        return headers

    def get_payload(self, phone: str) -> dict:
        return {"mobile": phone}