# Github : https://github.com/Bllare

import requests
from apis.status import SendStatus
from typing import Literal, List
from .abstract import AbstractSmsProvider
from abc import ABC
from abc import abstractmethod

PayloadStyle = Literal["json", "data", "params"]

class PostRequestSmsProvider(AbstractSmsProvider,ABC):
    """Base Abstract class for sms api calls"""
    
    name: str = "Base SMS"
    url: str = "https://example.com/send_sms"
    payload_type: PayloadStyle = "json" 

    def __init__(self):
        super().__init__()
        self._validate_class_variables()

    def _validate_class_variables(self) -> None:
        """Ensures that subclasses have properly set the required class variables"""
        if not self.name:
            raise ValueError(f"{self.__class__.__name__} must have a unique 'name'")
        
        if not self.url:
            raise ValueError(f"{self.__class__.__name__} must have a 'url' defined")
    
    def send_request(self, phone_number : str):
        headers = self.get_headers()
        payload = self.get_payload(phone_number)
        
        request_kwargs = {
            "method": "POST",
            "url": self.url,
            "headers": headers,
            "timeout": 10,
            self.payload_type: payload
        }

        return requests.request(**request_kwargs)

    
    @abstractmethod
    def get_payload(self, phone: str = None) -> dict | str:
        """Must be implemented by subclass"""
        pass