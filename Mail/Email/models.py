from django.db import models

# Create your models here.

class UserDetails(models.Model):
    fullname = models.CharField(max_length=50, verbose_name="Full Name")
    password = models.CharField(max_length=50, verbose_name="Password")
    email    = models.EmailField(max_length=254, verbose_name="Email")