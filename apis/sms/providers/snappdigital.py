from apis.sms.base import SmsProvider


class SmsSnappDigital(SmsProvider):
    name = "SMS Snapp Digital"
    url = "https://digitalsignup.snapp.ir/oauth/drivers/api/v1/otp"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {"cellphone": phone}

