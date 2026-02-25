# Github: https://github.com/Bllare
import re
import requests
from apis.sms.abstract import AbstractSmsProvider


class SmsModiseh(AbstractSmsProvider):
    name = "SMS Modiseh"

    def send_request(self, phone: str) -> requests.Response:
        session = requests.Session()
        # Load the login page to get the form_key
        page = "https://www.modiseh.com/customer/account/login/referer/aHR0cHM6Ly93d3cubW9kaXNlaC5jb20vY2F0ZWdvcnktYmVhdXR5Lw%3D%3D/"
        r = session.get(page, headers=self.get_headers(), timeout=10)
        # Extract form_key (usually in a hidden input)
        match = re.search(r'name="form_key"\s+value="([^"]+)"', r.text)
        if not match:
            raise Exception("Could not extract form_key")
        form_key = match.group(1)

        post_url = "https://www.modiseh.com/customer/account/loginpost/"
        payload = {
            "otp_code": "",
            "login[username]": "",
            "username": phone,
            "pass": "",
            "my_pass": "",
            "is_force_login": "",
            "customer_set_password": "",
            "customer_set_password2": "",
            "form_key": form_key,
            "type": "enter_mobile",
            "otpCall": "false",
            "captcha[user_login]": "123456",  # appears in HAR, maybe static
            "referer": "aHR0cHM6Ly93d3cubW9kaXNlaC5jb20vY2F0ZWdvcnktYmVhdXR5Lw==",
            "otp_token": ""
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["X-Requested-With"] = "XMLHttpRequest"
        return session.post(post_url, data=payload, headers=headers, timeout=10)