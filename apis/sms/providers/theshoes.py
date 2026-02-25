from apis.status import SendStatus
from apis.sms.base import PostRequestSmsProvider

class SmsTheshoes(PostRequestSmsProvider):
    name = "SMS Theshoes"
    url = "https://theshoes.ir/api/v1/sessions/login_request"
    payload_type = "json"

    def get_payload(self, phone: str) -> dict:
        return {
            "mobile_phone": phone
        }

    def handle_response(self, response):
        if response.status_code == 200:
            return SendStatus.SENT
        return super().handle_response(response)