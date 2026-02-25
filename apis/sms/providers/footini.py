# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Footini(SmsProvider):
    name = "SMS Footini"
    url = "https://footini.ir/wp-admin/admin-ajax.php"
    method = "POST"
    payload_type = "params"

    def get_payload(self, phone):
        return f"digt_countrycode=%2B98&phone={int(phone)}&digits_reg_name=&digits_reg_username=&digits_reg_password=&digits_process_register=1&signup_otp_mode=1&instance_id=&optional_data=optional_data&action=digits_forms_ajax&type=register&dig_otp=&digits=1&digits_redirect_page=%2F%2Ffootini.ir%2F%3Fredirect_to%26page%3D2&digits_form=e2fbbf62c8&_wp_http_referer=%2F%3Flogin%3Dtrue%26redirect_to%26page%3D2&container=digits_protected&sub_action=sms_otp"
    