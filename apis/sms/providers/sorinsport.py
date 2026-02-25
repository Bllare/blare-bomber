from apis.status import SendStatus
from apis.sms.base import PostRequestSmsProvider

class SmsSorinsport(PostRequestSmsProvider):
    name = "SMS Sorinsport"
    url = "https://sorinsport.com/wp-admin/admin-ajax.php"
    payload_type = "data"

    def get_headers(self):
        headers = super().get_headers()
        headers.update({
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest"
        })
        return headers

    def get_payload(self, phone: str) -> dict:
        return {
            "action": "voorodak__submit-username",
            "username": phone,
            "security": "f58a5872bc"
        }

    def handle_response(self, response):
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("success") and data.get("data", {}).get("sent"):
                    return SendStatus.SENT
            except:
                pass
        return super().handle_response(response)