from apis.status import SendStatus
from apis.sms.base import PostRequestSmsProvider

class SmsCactusleather(PostRequestSmsProvider):
    name = "SMS Cactusleather"
    url = "https://cactusleather.ir/cpr/registermobile"
    payload_type = "json"

    def get_headers(self):
        headers = super().get_headers()
        headers.update({
            "Content-Type": "application/json; charset=utf-8",
            "X-Requested-With": "XMLHttpRequest"
        })
        return headers

    def get_payload(self, phone: str) -> dict:
        return {
            "FullName": "name lastanme",
            "Mobile": phone,
            "IsMale": False,
            "Favorites": [],
            "Active": 1,
            "Addresses": {
                "Item": {
                    "Id": 0,
                    "StateId": -1,
                    "State": {},
                    "City": {},
                    "CityId": -1
                },
                "List": []
            },
            "IsOnline": False,
            "Grade": {"Id": 0},
            "IsRecover": False,
            "IsSmsSend": False,
            "Description": ""
        }

    def handle_response(self, response):
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("Code") == 1:
                    return SendStatus.SENT
            except:
                pass
        return super().handle_response(response)