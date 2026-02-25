# Github: https://github.com/Bllare
import re
import requests
from apis.sms.abstract import AbstractSmsProvider


class SmsMakyajgallery(AbstractSmsProvider):
    name = "SMS Makyajgallery"

    def send_request(self, phone: str) -> requests.Response:
        session = requests.Session()
        # Load the login page to get the CSRF token
        login_page = "https://makyajgallery.com/user/login"
        r = session.get(login_page, headers=self.get_headers(), timeout=10)
        # Extract CSRF token from meta tag (common in Laravel)
        match = re.search(r'name="csrf-token"\s+content="([^"]+)"', r.text)
        if not match:
            raise Exception("Could not extract CSRF token")
        csrf_token = match.group(1)

        post_url = "https://makyajgallery.com/ajax/send_sms_active"
        headers = self.get_headers()
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["X-Requested-With"] = "XMLHttpRequest"
        headers["X-CSRF-TOKEN"] = csrf_token

        payload = {"mobile": phone}
        return session.post(post_url, data=payload, headers=headers, timeout=10)