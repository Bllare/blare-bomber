# Github : https://github.com/Bllare

from apis.sms.base import PostRequestSmsProvider

class SmsMamifood(PostRequestSmsProvider):
    name = "SMS Mamifood"
    url = "https://mamifood.org/Registration.aspx/SendValidationCode"
    payload_type = "json" 


    def get_payload(self, phone):
        return {"Phone":phone,"did":""}

