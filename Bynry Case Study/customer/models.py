from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    REQUEST_CHOICES = [
        ('leak', 'Gas Leak'),
        ('billing', 'Billing Issue'),
        ('repair', 'Repair Request'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=10, choices=REQUEST_CHOICES)
    description = models.TextField()
    file_attachment = models.FileField(upload_to='service_requests/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')
    
    def __str__(self):
        return f"{self.get_request_type_display()} - {self.status}"
