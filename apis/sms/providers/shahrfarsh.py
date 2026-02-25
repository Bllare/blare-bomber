# Github : https://github.com/Bllare

from apis.sms.base import PostRequestSmsProvider

class SmsShahrfarsh(PostRequestSmsProvider):
    name = "SMS Shahrfarsh"
    url = "https://shahrfarsh.com/Account/Login"
    payload_type = "json"

    def get_payload(self, phone):
        return {"phoneNumber": phone}
    
