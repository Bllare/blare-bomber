# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class Tenzumusic(PostRequestSmsProvider):
    name = "SMS Tenzumusic"
    url = "https://napi.tenzumusic.com/user/auth/otp/generate"
    payload_type = "json"

    def get_payload(self, phone):
        return {
        "phone_number": phone,
        "country_code": "+98"
    }
    