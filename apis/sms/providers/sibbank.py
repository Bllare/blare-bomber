from apis.sms.base import SmsProvider

class SmsSibbank(SmsProvider):
    name = "SMS Sibbank"
    url = "https://api.sibbank.ir/v1/auth/login"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {"phone_number": phone}

