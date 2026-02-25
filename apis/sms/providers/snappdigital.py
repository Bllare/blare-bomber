# Github : https://github.com/Bllare

from apis.sms.base import PostRequestSmsProvider


class SmsSnappDigital(PostRequestSmsProvider):
    name = "SMS Snapp Digital"
    url = "https://digitalsignup.snapp.ir/oauth/drivers/api/v1/otp"
    payload_type = "json"

    def get_payload(self, phone):
        return {"cellphone": phone}

