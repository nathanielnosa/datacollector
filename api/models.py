from django.db import models
from django.contrib.auth.models import User

class DataField(models.Model):
    STATUS_CHOICES = [
        ('Done', 'Done'),
        ('Not Done', 'Not Done'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    volume_dispensed = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Done')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.amount_paid}"
