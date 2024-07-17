from django.urls import path
from services.otp.api.views import send_otp_email, verify_otp_email, send_otp_sms, verify_otp_sms

urlpatterns = [
    path('send-otp-email/', send_otp_email, name='send-otp-email'),
    path('verify-otp-email/', verify_otp_email, name='verify-otp-email'),
    path('send-otp-sms/', send_otp_sms, name='send-otp-sms'),
    path('verify-otp-sms/', verify_otp_sms, name='verify-otp-sms'),
]


# from django.urls import path
# from services.otp.api.views import SendOTPView, VerifyOTPView

# urlpatterns = [
#     path('send-otp/', SendOTPView.as_view(), name='send-otp'),
#     path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
# ]
