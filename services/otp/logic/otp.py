import pyotp
from django.core.cache import cache
from django.conf import settings
from django.core.mail import send_mail


class OTPService:
    def __init__(self, user):
        self.user = user
        self.secret = pyotp.random_base32()
        self.totp = pyotp.TOTP(self.secret)

    def generate_otp(self):
        otp = self.totp.now()
        otp_key = f"otp_{self.user.id}"
        cache.set(otp_key, otp, timeout=settings.CACHE_TTL)
        return otp

    def send_otp(self, email):
        otp = self.generate_otp()
        subject = 'Your OTP Code'
        message = f'Your OTP code is {otp}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)

    def verify_otp(self, otp):
        otp_key = f"otp_{self.user.id}"
        stored_otp = cache.get(otp_key)
        if stored_otp and stored_otp == otp:
            cache.delete(otp_key)
            return True
        return False


# class OTPService:
#     def __init__(self, user):
#         self.user = user
#         self.secret = pyotp.random_base32()
#         self.totp = pyotp.TOTP(self.secret)

#     def generate_otp(self):
#         otp = self.totp.now()
#         expiration_time = datetime.now() + timedelta(minutes=5)  # OTP valid for 5 minutes
#         OTP.objects.create(user=self.user, otp=otp, expires_at=expiration_time)
#         return otp

#     def send_otp(self, email):
#         otp = self.generate_otp()
#         subject = 'Your OTP Code'
#         message = f'Your OTP code is {otp}'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [email]
#         send_mail(subject, message, email_from, recipient_list)

#     def verify_otp(self, otp):
#         try:
#             otp_record = OTP.objects.get(user=self.user, otp=otp)
#             if otp_record.is_valid():
#                 return True
#             else:
#                 otp_record.delete()  # Clean up expired OTP
#                 return False
#         except OTP.DoesNotExist:
#             return False
