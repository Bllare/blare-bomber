from .base import SmsProvider
import apis.sms.providers  # 🔑 STATIC PACKAGE IMPORT

SMS_PROVIDERS = list(SmsProvider._registry)