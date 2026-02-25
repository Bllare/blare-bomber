# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Basalam(SmsProvider):
    name = "SMS Basalam"
    url = "https://services.basalam.com/web/v1/auth/captcha/otp-request"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {
        "mobile": phone,
        "client_id": "11",
        "login_by_backup_mobile": False
    }
    