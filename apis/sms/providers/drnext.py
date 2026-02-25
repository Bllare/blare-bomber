# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider


class SmsDrnext(PostRequestSmsProvider):
    name = "SMS Drnext"
    url = "https://cyclops.drnext.ir/v1/patients/auth/send-verification-token"
    payload_type = "json"

    def get_payload(self, phone):
        return {"source": "besina","mobile": phone}

