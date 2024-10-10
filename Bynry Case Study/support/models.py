from django.db import models
from customer.models import ServiceRequest

class Ticket(models.Model):
    request = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)
    assigned_support = models.ForeignKey(User, on_delete=models.CASCADE)
    resolution_notes = models.TextField(blank=True, null=True)
    resolved_on = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"Ticket for {self.request.id} assigned to {self.assigned_support.username}"
