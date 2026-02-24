from apis.sms.base import SmsProvider

class SmsSaapa(SmsProvider):
    name = "SMS Saapa"
    url = "https://uiapi2.saapa.ir/api/otp/sendCode"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return {"mobile": phone,"from_meter_buy": False}
