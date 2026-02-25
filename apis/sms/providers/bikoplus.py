from apis.status import SendStatus
from apis.sms.base import PostRequestSmsProvider

class SmsBikoplus(PostRequestSmsProvider):
    name = "SMS Bikoplus"
    url = "https://bikoplus.com/account/check-phone-number"
    payload_type = "json"

    def get_headers(self):
        headers = super().get_headers()
        headers["Content-Type"] = "application/json;charset=utf-8"
        return headers

    def get_payload(self, phone: str) -> dict:
        return {
            "phoneNumber": phone,
            "authenticationMode": None
        }

    def handle_response(self, response):
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("isSuccess") and data.get("statusCode") == 200:
                    return SendStatus.SENT
            except:
                pass
        return super().handle_response(response)