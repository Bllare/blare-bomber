from apis.status import SendStatus
from apis.sms.base import PostRequestSmsProvider
from apis.status import SendStatus

class SmsOffland(PostRequestSmsProvider):
    name = "SMS Offland"
    url = "https://offlandorg.com/wp-admin/admin-ajax.php"
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
            "action": "stm_login_register",
            "type": "mobile",
            "input": phone
        }

    def handle_response(self, response):
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("success"):
                    return SendStatus.SENT
            except:
                pass
        return super().handle_response(response)