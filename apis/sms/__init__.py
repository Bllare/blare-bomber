import pkgutil
import importlib
import os

providers_path = os.path.join(__path__[0], "providers")

for module in pkgutil.iter_modules([providers_path]):
    importlib.import_module(f"{__name__}.providers.{module.name}")

from .base import SmsProvider

SMS_PROVIDERS = [cls() for cls in SmsProvider._registry]