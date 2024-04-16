from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    company_name = models.CharField(max_length=15)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    
    def __str__(self):
        return self.username