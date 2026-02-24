# Github : https://github.com/Bllare

from apis.sms.base import SmsProvider

class SmsMamifood(SmsProvider):
    name = "SMS Mamifood"
    url = "https://mamifood.org/Registration.aspx/SendValidationCode"
    method = "POST"
    payload_type = "json" 


    def get_payload(self, phone):
        return {"Phone":phone,"did":""}

