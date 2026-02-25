# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Tenzumusic(SmsProvider):
    name = "SMS Tenzumusic"
    url = "https://napi.tenzumusic.com/user/auth/otp/generate"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {
        "phone_number": phone,
        "country_code": "+98"
    }
    