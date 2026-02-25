# Github : https://github.com/Bllare
from apis.sms.base import PostRequestSmsProvider

class IranianStyle(PostRequestSmsProvider):
    name = "SMS IranianStyle"
    url = "https://iranian-style.com/wp-admin/admin-ajax.php"
    payload_type = "data"

    def get_payload(self, phone):
        return {
        "action": "voorodak__submit-username",
        "username": phone,
        "security": "7b88cd2815"
    }
    