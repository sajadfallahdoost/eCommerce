import pyotp
from django.core.cache import cache
from django.conf import settings
from django.core.mail import send_mail
import requests
import logging
from rest_framework_simplejwt.tokens import RefreshToken

logger = logging.getLogger(__name__)


class OTPService:
    def __init__(self, user=None, phone_number=None):
        self.user = user
        self.phone_number = phone_number
        self.otp_key = "otp_secret_global"

        self.secret = cache.get(self.otp_key)
        if not self.secret:
            self.secret = pyotp.random_base32()
            cache.set(self.otp_key, self.secret, timeout=None)
            logger.debug(f"Generated and set new secret: {self.secret}")
        else:
            logger.debug(f"Retrieved existing secret: {self.secret}")

    def generate_otp(self):
        totp = pyotp.TOTP(self.secret)
        otp = totp.now()
        cache.set(self.otp_key, otp, timeout=settings.CACHE_TTL)
        return otp

    def send_otp_email(self, email):
        otp = self.generate_otp()
        subject = 'Your OTP Code'
        message = f'Your OTP code is: {otp}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)

    def send_otp_sms(self, phone_number):
        otp = self.generate_otp()
        url = "https://api.sms.ir/v1/send/verify"
        headers = {
            "x-api-key": "cwSvgHmGQsyQxbI4dOWxRQaAuIRT1k9Q49QrCBvpR9BOymXAKvjCC57fOaoM34AV",
            'ACCEPT': 'application/json',
            'Content-Type': 'application/json'
        }
        payload = {
            "mobile": phone_number,
            "templateId": 100000,
            "parameters": [
                {
                    "name": "CODE",
                    "value": otp
                }
            ]
        }
        response = requests.post(url, headers=headers, json=payload)

        response_data = response.json()
        if response_data.get('status') != 1:
            raise Exception("Failed to send OTP via SMS")
        return response_data

    def verify_otp(self, otp):
        stored_otp = cache.get(self.otp_key)
        logger.debug(f"Verifying OTP. Stored OTP: {stored_otp}, Provided OTP: {otp}")

        if stored_otp and stored_otp == otp:
            cache.delete(self.otp_key)
            return True
        return False

    @staticmethod
    def generate_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


# class OTPService:
#     def __init__(self, user=None, phone_number=None):
#         self.user = user
#         self.phone_number = phone_number
#         self.secret = self.get_secret()

#     def get_secret(self):
#         if self.user:
#             otp_key = f"otp_secret_{self.user.id}"
#         elif self.phone_number:
#             otp_key = f"otp_secret_{self.phone_number}"
#         else:
#             otp_key = "otp_secret_generic"

#         secret = cache.get(otp_key)
#         if not secret:
#             secret = pyotp.random_base32()
#             cache.set(otp_key, secret, timeout=None)
#             logger.debug(f"Generated and set new secret for key {otp_key}: {secret}")
#         else:
#             logger.debug(f"Retrieved existing secret for key {otp_key}: {secret}")
#         return secret

#     def generate_otp(self):
#         totp = pyotp.TOTP(self.secret)
#         otp = totp.now()
#         if self.user:
#             otp_key = f"otp_{self.user.id}"
#         elif self.phone_number:
#             otp_key = f"otp_{self.phone_number}"
#         else:
#             otp_key = "otp_generic"
#         # logger.debug(f"Storing OTP {otp} in cache with key {otp_key}")
#         cache.set(otp_key, otp, timeout=settings.CACHE_TTL)
#         # breakpoint()
#         return otp

#     # def generate_otp(self):
#     #     totp = pyotp.TOTP(self.secret)
#     #     otp = totp.now()
#     #     if self.user:
#     #         otp_key = f"otp_{self.user.id}"
#     #     elif self.phone_number:
#     #         otp_key = f"otp_{self.phone_number}"
#     #     else:
#     #         logger.error("OTP key generation failed: No user or phone number provided.")
#     #         raise ValueError("Cannot generate OTP key: No user or phone number provided.")

#     #     cache.set(otp_key, otp, timeout=settings.CACHE_TTL)
#     #     logger.debug(f"Stored OTP {otp} in cache with key {otp_key}")
#     #     return otp

#     def send_otp_email(self, email):
#         otp = self.generate_otp()
#         subject = 'Your OTP Code'
#         message = f'Your OTP code is: {otp}'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [email]
#         send_mail(subject, message, email_from, recipient_list)

#     def send_otp_sms(self, phone_number):
#         otp = self.generate_otp()
#         url = "https://api.sms.ir/v1/send/verify"
#         headers = {
#             "x-api-key": "cwSvgHmGQsyQxbI4dOWxRQaAuIRT1k9Q49QrCBvpR9BOymXAKvjCC57fOaoM34AV",
#             'ACCEPT': 'application/json',
#             'Content-Type': 'application/json'
#         }
#         payload = {
#             "mobile": phone_number,
#             "templateId": 100000,
#             "parameters": [
#                 {
#                     "name": "CODE",
#                     "value": otp
#                 }
#             ]
#         }
#         response = requests.post(url, headers=headers, json=payload)

#         # logger.debug(f"SMS API Response: {response.status_code} - {response.text}")
#         response_data = response.json()
#         # logger.debug(f"Full SMS API Response Data: {response_data}")
#         if response_data.get('status') != 1:
#             raise Exception("Failed to send OTP via SMS")
#         return response_data

#     def verify_otp(self, otp):
#         otp_key = None
#         if self.user:
#             otp_key = f"otp_{self.user.id}"
#         elif self.phone_number:
#             otp_key = f"otp_{self.phone_number}"
#         else:
#             otp_key = "otp_generic"

#         stored_otp = cache.get(otp_key)
#         logger.debug(f"Verifying OTP. Key: {otp_key}, Stored OTP: {stored_otp}, Provided OTP: {otp}")

#         if stored_otp and stored_otp == otp:
#             cache.delete(otp_key)
#             return True
#         return False

#     @staticmethod
#     def generate_tokens_for_user(user):
#         refresh = RefreshToken.for_user(user)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }
