# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider


class SmsElecmarket(SmsProvider):
    name = "SMS Elecmarket"
    url = "https://elecmarket.ir/wp-admin/admin-ajax.php"
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone):
        return f"action=stm_login_register&type=mobile&input={phone}"

    def get_headers(self):
        headers = super().get_headers()
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        return headers
    
    
