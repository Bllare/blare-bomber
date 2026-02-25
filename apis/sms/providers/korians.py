# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Korians(SmsProvider):
    name = "SMS Korians"
    url = "https://korians.com/wp-admin/admin-ajax.php"
    method = "POST"
    payload_type = "data"

    def get_payload(self, phone):
        return  {
        "action": "identifier_ajax_handler",
        "nonce": "8d2deda4ea",
        "data": f"farazsms_nonce=30d1be81b6&_wp_http_referer=%252Fmy-account%252F&identifier={phone}&back_url="
    }
    