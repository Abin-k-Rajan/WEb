from django.db import models

# Create your models here.
class feedback(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    desc = models.TextField()