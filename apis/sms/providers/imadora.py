# Github: https://github.com/Bllare
import re
import requests
from apis.sms.abstract import AbstractSmsProvider


class SmsImadora(AbstractSmsProvider):
    name = "SMS Imadora"

    def send_request(self, phone: str) -> requests.Response:
        session = requests.Session()
        # Load the auth page to get the security nonce
        auth_page = "https://imadora.ir/auth/"
        r = session.get(auth_page, headers=self.get_headers(), timeout=10)
        # Extract the security nonce (value of the 'security' parameter)
        match = re.search(r'security["\']?\s*:\s*["\']([a-f0-9]+)["\']', r.text)
        if not match:
            # Alternatively, look for it in a hidden input
            match = re.search(r'name="security"\s+value="([^"]+)"', r.text)
        if not match:
            raise Exception("Could not extract security nonce")
        security = match.group(1)

        post_url = "https://imadora.ir/wp-admin/admin-ajax.php"
        payload = {
            "action": "voorodak__submit-username",
            "username": phone,
            "security": security
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["X-Requested-With"] = "XMLHttpRequest"
        return session.post(post_url, data=payload, headers=headers, timeout=10)