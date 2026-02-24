from apis.sms.base import SmsProvider

class SmsDastkhatIsad(SmsProvider):
    name = "SMS DastkhatIsad"
    url = "https://dastkhat-isad.ir/api/v1/user/store"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone: str) -> dict:
        return {"mobile": f"+98{int(phone)}","countryCode": 98,"device_os": 2}

