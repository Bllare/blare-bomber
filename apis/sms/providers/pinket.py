from apis.sms.base import SmsProvider

class SmsPinket(SmsProvider):
    name = "SMS Pinket"
    url = "https://pinket.com/api/cu/v2/phone-verification"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return  {"phoneNumber": phone}
