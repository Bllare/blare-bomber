# Github: https://github.com/Bllare
import re
import requests
from apis.sms.abstract import AbstractSmsProvider
from apis.status import SendStatus


class SmsArayeshiVarani(AbstractSmsProvider):
    name = "SMS Arayeshi Varani"

    def send_request(self, phone: str) -> requests.Response:
        session = requests.Session()
        # First, load the login page to obtain the CSRF token and session cookies
        login_page_url = "https://arayeshi-varani.com/auth/login"
        r = session.get(login_page_url, headers=self.get_headers(), timeout=10)
        # Extract _token from the HTML (it's inside a hidden input)
        match = re.search(r'name="_token"\s+value="([^"]+)"', r.text)
        if not match:
            raise Exception("Could not extract CSRF token")
        token = match.group(1)

        # Now send the OTP request
        post_url = "https://arayeshi-varani.com/auth/login"
        payload = {
            "_token": token,
            "phone": phone
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        # Important: use the same session to preserve cookies
        return session.post(post_url, data=payload, headers=headers, timeout=10)