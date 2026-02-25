# Github: https://github.com/Bllare
import re
import requests
from apis.sms.abstract import AbstractSmsProvider


class SmsModiage(AbstractSmsProvider):
    name = "SMS Modiage"

    def send_request(self, phone: str) -> requests.Response:
        session = requests.Session()
        # Load the auth page to get the CSRF token
        auth_page = "https://modiage.com/auth"
        r = session.get(auth_page, headers=self.get_headers(), timeout=10)
        # Extract the _token from the form
        match = re.search(r'name="_token"\s+value="([^"]+)"', r.text)
        if not match:
            raise Exception("Could not extract CSRF token")
        token = match.group(1)

        post_url = "https://modiage.com/auth/verify"
        payload = {
            "_token": token,
            "mobile": phone
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["X-Requested-With"] = "XMLHttpRequest"
        return session.post(post_url, data=payload, headers=headers, timeout=10)