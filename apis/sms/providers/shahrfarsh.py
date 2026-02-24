# Github : https://github.com/Bllare

from apis.sms.base import SmsProvider

class SmsShahrfarsh(SmsProvider):
    name = "SMS Shahrfarsh"
    url = "https://shahrfarsh.com/Account/Login"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {"phoneNumber": phone}
    
