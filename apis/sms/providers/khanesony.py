
from apis.sms.base import PostRequestSmsProvider
from apis.status import SendStatus

class KhaneSony(PostRequestSmsProvider):
    name = "SMS Khanesony"
    url = "https://khanesony.co/wp-admin/admin-ajax.php"
    payload_type = "json"

    def get_payload(self, phone):
        return  {
        "action": "rml_operation",
        "nonce": "12556efe66",
        "data[0][name]": "rml-login-type",
        "data[0][value]": "mobile",
        "data[1][name]": "login-mobile",
        "data[1][value]": phone,
        "data[2][name]": "rml-mobile-dial-code",
        "data[2][value]": "98",
        "data[3][name]": "rml-mobile-country-code",
        "data[3][value]": "ir",
        "data[4][name]": "rml-operation",
        "data[4][value]": "login",
        "data[5][name]": "rml-redirect",
        "data[5][value]": ""
    } 
        
    def handle_response(self, response):
        if response.json()['success']:
            return SendStatus.SENT
        
        return SendStatus.UNKNOWN
