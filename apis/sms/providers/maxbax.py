from apis.status import SendStatus
from apis.sms.base import PostRequestSmsProvider

class SmsMaxbax(PostRequestSmsProvider):
    name = "SMS Maxbax"
    url = "https://maxbax.com/bakala/ajax/send_code/"
    payload_type = "data"

    def get_headers(self):
        headers = super().get_headers()
        headers.update({
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-CSRF-TOKEN": "aa9cfa0528",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://maxbax.com/product-category/%D9%85%D8%B1%D8%AF%D8%A7%D9%86%D9%87/%DA%A9%D9%81%D8%B4-%D9%88-%DA%A9%D8%AA%D8%A7%D9%86%DB%8C/"
        })
        return headers

    def get_payload(self, phone: str) -> dict:
        return {
            "action": "bakala_send_code",
            "phone_email": phone
        }