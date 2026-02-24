from apis.sms.base import SmsProvider

class SmsSnapp(SmsProvider):
    name = "SMS Snapp"
    url = "https://app.snapp.taxi/api/api-passenger-oauth/v3/mutotp"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return  {"cellphone":f"+98{int(phone)}","attestation":{"method":"skip","platform":"skip"},"extra_methods":[]}
