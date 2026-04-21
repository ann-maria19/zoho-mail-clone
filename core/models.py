from django.db import models
from django.contrib.auth.models import User

class Email(models.Model):  # <--- Check this spelling!
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_emails")
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)