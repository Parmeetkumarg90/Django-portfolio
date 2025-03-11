from django.db import models

# Create your models here.
class contact_data(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_phone = models.CharField(max_length=100)
    user_message = models.TextField(max_length=1000)