# Github : https://github.com/Bllare
from apis.sms.base import SmsProvider

class SmsRefahtea(SmsProvider):
    name = "SMS Refahtea"
    url = "https://refahtea.ir/wp-admin/admin-ajax.php"
    method = "POST"
    payload_type = "data"

    def get_payload(self, phone):
        return f"digt_countrycode=%2B98&phone={int(phone)}&digits_process_register=1&sms_otp=&otp_step_1=1&digits_otp_field=1&instance_id=&optional_data=optional_data&action=digits_forms_ajax&type=register&dig_otp=sms_otp&digits=1&digits_redirect_page=%2F%2Frefahtea.ir%2F&digits_form=5019a03393&_wp_http_referer=%2F&otp_resend=true&container=digits_protected&sub_action=sms_otp"

