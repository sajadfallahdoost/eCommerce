# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone


# class OTP(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     otp = models.CharField(max_length=6)
#     created_at = models.DateTimeField(auto_now_add=True)
#     expires_at = models.DateTimeField()

#     def is_valid(self):
#         return timezone.now() < self.expires_at
