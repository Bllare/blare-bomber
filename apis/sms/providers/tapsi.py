from apis.sms.base import SmsProvider

class SmsTapsi(SmsProvider):
    name = "SMS Tapsi"
    url = "https://api.tapsi.ir/api/v2.2/user"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {"credential": {"phoneNumber": phone, "role": "DRIVER"}, "otpOption": "SMS"}

