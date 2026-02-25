# Github: https://github.com/Bllare
import re
import requests
from apis.sms.abstract import AbstractSmsProvider


class SmsNasimshop(AbstractSmsProvider):
    name = "SMS Nasimshop"

    def send_request(self, phone: str) -> requests.Response:
        session = requests.Session()
        # Load the signin page to get security nonce
        page = "https://nasimshop.com/signin/"
        r = session.get(page, headers=self.get_headers(), timeout=10)
        match = re.search(r'security["\']?\s*:\s*["\']([a-f0-9]+)["\']', r.text)
        if not match:
            match = re.search(r'name="security"\s+value="([^"]+)"', r.text)
        if not match:
            raise Exception("Could not extract security nonce")
        security = match.group(1)

        post_url = "https://nasimshop.com/wp-admin/admin-ajax.php"
        payload = {
            "action": "voorodak__submit-username",
            "username": phone,
            "security": security
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["X-Requested-With"] = "XMLHttpRequest"
        return session.post(post_url, data=payload, headers=headers, timeout=10)