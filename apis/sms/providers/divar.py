from apis.sms.base import SmsProvider

class SmsDivar(SmsProvider):
    name = "SMS Divar"
    url = "https://api.divar.ir/v5/auth/authenticate"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {"phone":str(int(phone))}
