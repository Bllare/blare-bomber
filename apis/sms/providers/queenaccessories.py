from apis.sms.base import SmsProvider

class SmsQueenaccessories(SmsProvider):
    name = "SMS Queenaccessories"
    url = "https://queenaccessories.ir/api/v1/sessions/login_request"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {"mobile_phone": phone}
