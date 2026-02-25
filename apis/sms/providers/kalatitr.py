from apis.status import SendStatus
from apis.sms.base import PostRequestSmsProvider

class SmsKalatitr(PostRequestSmsProvider):
    name = "SMS Kalatitr"
    url = "https://kalatitr.com/api/auth/otp"
    payload_type = "json"

    def get_payload(self, phone: str) -> dict:
        return {
            "mobile": phone
        }

    def handle_response(self, response):
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("isSuccess"):
                    return SendStatus.SENT
            except:
                pass
        return super().handle_response(response)