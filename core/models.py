from django.db import models
from django.contrib.auth.models import User

class Email(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_emails")
    recipient_email = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_emails")
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False) 

    def __str__(self):
        return self.subjecty 