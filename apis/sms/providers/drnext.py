# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider


class SmsDrnext(SmsProvider):
    name = "SMS Drnext"
    url = "https://cyclops.drnext.ir/v1/patients/auth/send-verification-token"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {"source": "besina","mobile": phone}

