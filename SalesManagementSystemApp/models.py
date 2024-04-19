from django.db import models

class Customer(models.Model):
    """Model for Customer Class"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    company_name = models.CharField(max_length=15)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    
    def __str__(self):
        return self.username
        
class Admin(models.Model):
    """Model for Admin class"""
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    def __str__(self):
        return str(self.username)

class Stage(models.Model):
    """Model for Stage Class"""
    custom_stage = models.CharField(max_length=150)
    def __str__(self):
        return str(self.custom_stage)
        
class CustServiceStage(models.Model):
    """Model for Cust Service Class"""
    custom_stage = models.CharField(max_length=150)
    def __str__(self):
        return str(self.custom_stage)
        
class ITStage(models.Model):
    """Model for IT Stage Class"""
    custom_stage = models.CharField(max_length=150)
    def __str__(self):
        return str(self.custom_stage)
        
class SalesStage(models.Model):
    """Model for Sales Stage Class"""
    custom_stage = models.CharField(max_length=150)
    def __str__(self):
        return str(self.custom_stage)
        
class RDStage(models.Model):
    """Model for R&D Stage Class"""
    custom_stage = models.CharField(max_length=150)
    def __str__(self):
        return str(self.custom_stage)