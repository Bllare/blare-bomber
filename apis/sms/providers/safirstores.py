# Github: https://github.com/Bllare
import requests
from apis.sms.abstract import AbstractSmsProvider


class SmsSafirstores(AbstractSmsProvider):
    name = "SMS Safirstores"

    def send_request(self, phone: str) -> requests.Response:
        session = requests.Session()
        # First, visit a category page to obtain cookies (deviceId, etc.)
        category_page = "https://www.safirstores.com/category/cosmetic"
        session.get(category_page, headers=self.get_headers(), timeout=10)

        post_url = "https://www.safirstores.com/api"
        # The HAR uses Content-Type: text/plain, but we can use application/json
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        payload = {
            "apiRoute": "auth/login",
            "finalObj": {
                "input": phone
            }
        }
        return session.post(post_url, json=payload, headers=headers, timeout=10)