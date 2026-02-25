# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class Ilozi(SmsProvider):
    name = "SMS Ilozi"
    url = "https://ilozi.com/wp-admin/admin-ajax.php"
    method = "POST"
    payload_type = "params"

    def get_payload(self, phone):
        return f"login_digt_countrycode=%2B98&digits_phone={int(phone)}&action_type=phone&sms_otp=&otp_step_1=1&digits_otp_field=1&digits=1&instance_id=&action=digits_forms_ajax&type=login&digits_step_1_type=&digits_step_1_value=&digits_step_2_type=&digits_step_2_value=&digits_step_3_type=&digits_step_3_value=&digits_login_email_token=&digits_redirect_page=%2F%2Filozi.com%2F%3Fredirect_to%26page%3D1&digits_form=9451f06709&_wp_http_referer=%2F%3Flogin%3Dtrue%26redirect_to%26page%3D1&show_force_title=1&otp_resend=true&container=digits_protected&sub_action=sms_otp"
    