from abc import ABC, abstractmethod
import requests
from typing import List
from fake_headers import Headers
from apis.status import SendStatus
import inspect

class AbstractSmsProvider(ABC):
    """Base Abstract class for sms api calls"""

    _registry: List[type["AbstractSmsProvider"]] = [] # Used To Register subclasses dynamically 

    def __init__(self):
        self.headers_gen = Headers(browser="chrome", os="win", headers=True)
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # Skip base class itself
        if cls is AbstractSmsProvider:
            return

        # Only register concrete (non-abstract) subclasses
        if not inspect.isabstract(cls): 
            AbstractSmsProvider._registry.append(cls)

    @abstractmethod
    def send_request(self, phone_number: str) -> requests.Request:
        """Sends an SMS to the specified phone number. This method must be implemented by subclasses to define the specific API call logic.
        Args:
            phone_number (str): The target phone number to which the SMS should be sent.
        Returns:
            requests.Request: The request object that was sent.
        NOTE: 
            the method should return the request object that was sent.
        """
        pass


    def get_headers(self) -> dict:
        """Generates a random headers by default using fake_headers library"""
        return self.headers_gen.generate()
    

    def send(self, phone: str) -> SendStatus:
        """"Default send method works with most APIs, can be overridden by subclass if needed in some cases"""
        try:
            response = self.send_request(phone)
            return self.handle_response(response)
            
        except Exception as e:
            return SendStatus.ERROR


    def handle_response(self, response: requests.Response) -> SendStatus:
        """Default response handler, can be overridden by subclass if needed"""
        if response.status_code == 200:
            return SendStatus.SENT
        elif response.status_code == 429:
            return SendStatus.FAILED
        return SendStatus.UNKNOWN

    

    