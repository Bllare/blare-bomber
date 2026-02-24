# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider


class SmsGapfilm(SmsProvider):
    name = "SMS Gapfilm"
    url = "https://core.gapfilm.ir/api/v3.1/Account/Login"
    method = "POST"
    payload_type = "json" 


    def get_payload(self, phone):
        return {"Type": 3, "Username": "+98"+str(int(phone)), "SourceChannel": "GF_WebSite"}
