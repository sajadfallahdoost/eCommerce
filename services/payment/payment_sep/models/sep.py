from django.db import models
from django.utils import timezone


class Payment(models.Model):
    terminal_id = models.CharField(max_length=100)
    amount = models.BigIntegerField()
    res_num = models.CharField(max_length=100)
    ref_num = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.res_num} - {self.status}"
