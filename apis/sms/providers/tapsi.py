# Github : https://github.com/Bllare

from apis.sms.base import PostRequestSmsProvider

class SmsTapsi(PostRequestSmsProvider):
    name = "SMS Tapsi"
    url = "https://api.tapsi.ir/api/v2.2/user"
    payload_type = "json"

    def get_payload(self, phone):
        return {"credential": {"phoneNumber": phone, "role": "DRIVER"}, "otpOption": "SMS"}

