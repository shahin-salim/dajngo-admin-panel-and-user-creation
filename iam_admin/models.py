from django.db import models

class upUserModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    passowrd1 = models.CharField(max_length=100, null=True, blank=True,default=None)
    passowrd2 = models.CharField(max_length=100, null=True, blank=True,default=None)

    
