# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider


class SmsGapfilm(PostRequestSmsProvider):
    name = "SMS Gapfilm"
    url = "https://core.gapfilm.ir/api/v3.1/Account/Login"
    payload_type = "json" 


    def get_payload(self, phone):
        return {"Type": 3, "Username": "+98"+str(int(phone)), "SourceChannel": "GF_WebSite"}
