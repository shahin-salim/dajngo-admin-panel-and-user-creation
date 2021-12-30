from django.db import models

class upUserModel(models.Model):
    first_name = models.CharField(max_length=30, blank=True,default=None)
    last_name = models.CharField(max_length=30, blank=True,default=None)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, blank=True,default=None)
    password1 = models.CharField(max_length=100, null=True, blank=True,default=None)
    password2 = models.CharField(max_length=100, null=True, blank=True,default=None)
    

