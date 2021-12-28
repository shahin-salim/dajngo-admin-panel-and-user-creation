from django import forms  
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms.widgets import PasswordInput
from .models import upUserModel

class updateUser(forms.ModelForm):  
    
    class Meta:  
        model = User  
        fields = ['first_name','last_name','username', 'email']

class editUser(forms.ModelForm):
    class Meta:
        model = upUserModel
        fields = "__all__"



