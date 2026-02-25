# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class SmsDastkhatIsad(PostRequestSmsProvider):
    name = "SMS DastkhatIsad"
    url = "https://dastkhat-isad.ir/api/v1/user/store"
    payload_type = "json"

    def get_payload(self, phone: str) -> dict:
        return {"mobile": f"+98{int(phone)}","countryCode": 98,"device_os": 2}

