import pyotp
import random
import string
from django.core.mail import send_mail
from django.conf import settings


class OTPService:
    def __init__(self, secret=None):
        if secret is None:
            secret = self.generate_secret()
        self.secret = secret
        self.totp = pyotp.TOTP(self.secret)

    @staticmethod
    def generate_secret(length=16):
        # Generate a random base32 secret
        return ''.join(random.choice(string.ascii_uppercase + '234567') for _ in range(length))

    def send_otp(self, email):
        otp = self.totp.now()
        subject = 'Your OTP Code'
        message = f'Your OTP code is {otp}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        return otp

    def verify_otp(self, otp):
        return self.totp.verify(otp)
