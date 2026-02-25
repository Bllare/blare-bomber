# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Monjou(SmsProvider):
    name = "SMS Monjou"
    url = "https://monjou.ir/wp-admin/admin-ajax.php"
    method = "POST"
    payload_type = "data"

    def get_payload(self, phone):
        return  {
        "login_digt_countrycode": "+98",
        "digits_phone": str(int(phone)),
        "action_type": "phone",
        "signup_otp_mode": "1",
        "rememberme": "1",
        "digits": "1",
        "instance_id": "",
        "action": "digits_forms_ajax",
        "type": "login",
        "digits_step_1_type": "",
        "digits_step_1_value": "",
        "digits_step_2_type": "",
        "digits_step_2_value": "",
        "digits_step_3_type": "",
        "digits_step_3_value": "",
        "digits_login_email_token": "",
        "digits_redirect_page": "https://monjou.ir/my-account/",
        "digits_form": "333c7345f9",
        "_wp_http_referer": "/?login=true&redirect_to=https%253A%252F%252Fmonjou.ir%252Fmy-account%252F%26page%3D1",
        "show_force_title": "1",
        "container": "digits_protected",
        "sub_action": "sms_otp"
    }
    