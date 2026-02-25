from apis.sms.base import PostRequestSmsProvider
from apis.status import SendStatus

class SmsMellishoes(PostRequestSmsProvider):
    name = "SMS Mellishoes"
    url = "https://mellishoes.ir/auth/?endp=step-2"
    payload_type = "data"

    def get_headers(self):
        headers = super().get_headers()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        return headers

    def get_payload(self, phone: str) -> dict:
        return {
            "redirect_to": "",
            "action": "nirweb_panel_login_form",
            "nirweb_panel_username": phone
        }

    def handle_response(self, response):
        if response.status_code == 200:
            return SendStatus.SENT
        return super().handle_response(response)