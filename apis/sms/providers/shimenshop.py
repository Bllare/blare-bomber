# Github: https://github.com/Bllare
import requests
from apis.sms.abstract import AbstractSmsProvider


class SmsShimenshop(AbstractSmsProvider):
    name = "SMS Shimenshop"

    def send_request(self, phone: str) -> requests.Response:
        session = requests.Session()
        # First, visit the login page to obtain a session cookie
        login_page = "https://shimenshop.com/login"
        session.get(login_page, headers=self.get_headers(), timeout=10)

        # Now send the OTP request
        post_url = "https://shimenshop.com/login/?sendOTPCode=1"
        payload = {
            "username": phone,
            "isRegister": "1"
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["X-Requested-With"] = "XMLHttpRequest"
        return session.post(post_url, data=payload, headers=headers, timeout=10)