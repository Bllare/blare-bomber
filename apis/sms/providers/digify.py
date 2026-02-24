from apis.sms.base import SmsProvider

class SmsDigify(SmsProvider):
    name = "SMS Digify"
    url = "https://backend.digify.shop/user/merchant/otp/"
    method = "POST"
    payload_type = "json"

    def get_headers(self):
        headers = super().get_headers()
        headers["Content-Type"] = "application/json"
        return headers
    
    def get_payload(self, phone: str) -> dict:
        return {"phone_number": phone}
