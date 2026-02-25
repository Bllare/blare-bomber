# Github : https://github.com/Bllare

from apis.sms.base import PostRequestSmsProvider

class SmsSnappMarket(PostRequestSmsProvider):
    name = "SMS Snapp Market"
    url = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass"
    payload_type = "params"

    def get_payload(self, phone):
        return {"cellphone": phone}
