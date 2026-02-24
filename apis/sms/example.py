# Example SMS provider implementation - This is a template to show how to create a new SMS provider by inheriting from the base class.

from apis.sms.base import SmsProvider  
from apis.status import SendStatus

class ExampleSmsProvider(SmsProvider):
    """Example SMS provider that simulates sending SMS"""
    
    name = "Example SMS Provider"
    url = "https://example.com/auth/login"  # Replace with your real API endpoint
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone: str) -> dict:
        """Prepare the payload for sending SMS"""
        return {
            "phone": phone,
            "message": "Hello! This is a test message."
        }

    def handle_response(self, response):
        """Optional: override to customize response handling"""
        if response.status_code == 200:
            print("Response received:", response.json())
            return SendStatus.SENT
        return super().handle_response(response)


# --------------------------------------------------------
# NOTE:
# 1. To create a new custom SMS provider, simply create a new Python file
#    in the `providers` folder 
# 2. Make sure your class inherits from `SmsProvider`.
# 3. Once you do that, it will automatically be added to SmsProvider._registry
#    and can be used just like any other provider.
# --------------------------------------------------------