# Example SMS provider implementation - This is a template to show how to create a new SMS provider by inheriting from the base class.

from apis.sms.base import PostRequestSmsProvider  
from apis.status import SendStatus
from apis.sms.abstract import AbstractSmsProvider
import requests

class ExampleSmsProviderWithPostRequest(PostRequestSmsProvider):
    """
    Example SMS provider that simulates sending SMS
    This class can be used for apis that require a POST request with a payload type of json or data.
    """
    
    name = "Example SMS Provider"
    url = "https://example.com/auth/login"  # 
    method = "POST"
    payload_type = "json"

    def get_payload(self, phone: str) -> dict:
        """You will override this method to return the appropriate payload for the target API."""
        return {
            "phone": phone,
            "message": "Hello! This is a test message."
        }

    def handle_response(self, response):
        """Optional: override this method if you want custom handling based on the api's response structure."""
        if response.status_code == 200:
            return SendStatus.SENT
        return super().handle_response(response)

class ExampleSmsProvider(AbstractSmsProvider):
    """
    Example SMS provider that simulates sending SMS
    This class can be used for apis that require a GET request or you need further customization that doesn't fit the PostRequestSmsProvider structure.
    """

    def send_request(self, phone: str) -> requests.Request:
        """
        You will override this method to implement the logic for sending SMS using the target API.
        NOTE:
            it should return a requests.Request object
        """
        
        # Example implementation (you will replace this with actual API calls)
        return requests.get("GET", f"https://example.com/send?phone={phone}")