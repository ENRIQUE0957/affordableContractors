from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=260)
    email = models.EmailField()
    verify_email = models.EmailField()