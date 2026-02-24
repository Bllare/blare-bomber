# Github : https://github.com/Bllare

from apis.sms.base import SmsProvider

class SmsSnappMarket(SmsProvider):
    name = "SMS Snapp Market"
    url = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass"
    method = "POST" 
    payload_type = "params"

    def get_payload(self, phone):
        return {"cellphone": phone}
