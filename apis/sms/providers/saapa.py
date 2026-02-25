# Github : https://github.com/Bllare

from apis.sms.base import PostRequestSmsProvider

class SmsSaapa(PostRequestSmsProvider):
    name = "SMS Saapa"
    url = "https://uiapi2.saapa.ir/api/otp/sendCode"
    payload_type = "json"

    def get_payload(self, phone):
        return {"mobile": phone,"from_meter_buy": False}
