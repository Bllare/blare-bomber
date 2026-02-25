from apis.status import SendStatus
from apis.sms.base import PostRequestSmsProvider

class SmsJeanswest(PostRequestSmsProvider):
    name = "SMS Jeanswest"
    url = "https://api.jeanswest.ir/api/v1/otp/request/"
    payload_type = "json"

    def get_headers(self):
        headers = super().get_headers()
        headers.update({
            "platform": "3",
            "Authorization": ""
        })
        return headers

    def get_payload(self, phone: str) -> dict:
        # Remove leading 0 if present
        if phone.startswith("0"):
            phone = phone[1:]
        return {
            "phoneNumber": phone
        }

    def handle_response(self, response):
        if response.status_code == 201:
            try:
                data = response.json()
                if data.get("statusCode") == 200:
                    return SendStatus.SENT
            except:
                pass
        return super().handle_response(response)