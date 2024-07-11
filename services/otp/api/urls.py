from django.urls import path
from services.otp.api.views import send_otp, verify_otp

urlpatterns = [
    path('send-otp/', send_otp, name='send-otp'),
    path('verify-otp/', verify_otp, name='verify-otp'),
]


# from django.urls import path
# from services.otp.api.views import SendOTPView, VerifyOTPView

# urlpatterns = [
#     path('send-otp/', SendOTPView.as_view(), name='send-otp'),
#     path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
# ]
