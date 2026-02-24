# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider


class SmsKomodaa(SmsProvider):
    name = "SMS Komodaa"
    url = "https://api.komodaa.com/api/v2.6/loginRC/request"
    method = "POST"
    payload_type = "json" 


    def get_payload(self, phone):
        return  {"phone_number": phone}
    
 