from .abstract import AbstractSmsProvider
import apis.sms.providers  # 🔑 STATIC PACKAGE IMPORT

SMS_PROVIDERS = list(AbstractSmsProvider._registry)