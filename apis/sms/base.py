# Github : https://github.com/Bllare

from abc import ABC, abstractmethod
import requests
from fake_headers import Headers
from apis.status import SendStatus
from typing import Literal


PayloadStyle = Literal["json", "data", "params"]


class SmsProvider(ABC):
    """Base Abstract class for sms api calls"""
    _registry: list[type["SmsProvider"]] = [] # Used To Register subclasses dynamically 

    name: str = "Base SMS"
    url: str = None
    method: str = "POST"
    payload_type: PayloadStyle = "json" 


    def __init_subclass__(cls, **kwargs):
        """Automatically Adds subclasses that uses this calss as a parent in the _registry list"""
        super().__init_subclass__(**kwargs)
        if cls is SmsProvider: # ingoring the base class
            return
        if not getattr(cls, "__abstractmethods__", False):
            SmsProvider._registry.append(cls)

    def __init__(self):
        self.headers_gen = Headers(browser="chrome", os="win", headers=True)
        self._validate_class_variables()

    def _validate_class_variables(self) -> None:
        """Ensures that subclasses have properly set the required class variables"""

        if not self.name or self.name == "Base SMS":
            raise ValueError(f"{self.__class__.__name__} must have a unique 'name'")
        
        if not self.url:
            raise ValueError(f"{self.__class__.__name__} must have a 'url' defined")
        

    def get_headers(self) -> dict:
        """Generates a random headers by default using fake_headers library"""
        return self.headers_gen.generate()

    def handle_response(self, response: requests.Response) -> SendStatus:
        """Default response handler, can be overridden by subclass if needed"""
        if response.status_code == 200:
            return SendStatus.SENT
        elif response.status_code == 429:
            return SendStatus.FAILED
        return SendStatus.UNKNOWN
    

    def send(self, phone: str) -> SendStatus:
        """"Default send method works with most APIs, can be overridden by subclass if needed in some cases"""
        try:
            headers = self.get_headers()
            payload = self.get_payload(phone)
            
            request_kwargs = {
                "method": self.method.upper(),
                "url": self.url,
                "headers": headers,
                "timeout": 10,
                self.payload_type: payload
            }

            response = requests.request(**request_kwargs)
            return self.handle_response(response)
            
        except Exception as e:
            return SendStatus.ERROR
        
    @abstractmethod
    def get_payload(self, phone: str) -> dict | str:
        """Must be implemented by subclass"""
        pass