# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider


class SmsKomodaa(PostRequestSmsProvider):
    name = "SMS Komodaa"
    url = "https://api.komodaa.com/api/v2.6/loginRC/request"
    payload_type = "json" 


    def get_payload(self, phone):
        return  {"phone_number": phone}
    
 