# Github : https://github.com/Bllare

from apis.sms.base import PostRequestSmsProvider

class SmsSnapp(PostRequestSmsProvider):
    name = "SMS Snapp"
    url = "https://app.snapp.taxi/api/api-passenger-oauth/v3/mutotp"
    payload_type = "json"

    def get_payload(self, phone):
        return  {"cellphone":f"+98{int(phone)}","attestation":{"method":"skip","platform":"skip"},"extra_methods":[]}
