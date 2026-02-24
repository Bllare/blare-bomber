# Github : https://github.com/Bllare

from apis.sms.base import SmsProvider


class SmsTelketab(SmsProvider):
    name = "SMS Telketab"
    url = "https://telketab.com/otp_field/check_secret"
    method = "POST"
    payload_type = "data"

    def get_headers(self):
        headers = super().get_headers()
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        return headers
    
    def get_payload(self, phone):
        return f"identity={phone}&secret=&plugin=otp_field_sms_processor&key=otp_field_user_auth_form__otp_sms"
    