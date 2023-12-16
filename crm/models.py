from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Info(models.Model):
    org_name = models.CharField(max_length=64)
    address = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.org_name}"

class Events(models.Model):
    eventName = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    org_information = models.ForeignKey(Info, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Events"

    def __str__(self):
        return self.eventName
    