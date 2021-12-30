from django import forms  
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms.widgets import PasswordInput
from .models import upUserModel

userId = ''
# class updateUser(forms.ModelForm):  
    
#     class Meta:  
#         model = User  
#         fields = ['first_name','last_name','username', 'email']

#     def clean(self):
#         cleaned_data = super().clean()
#         email = cleaned_data.get("email")

#         if User.objects.filter(email=email).exists():
#             self.add_error('email', 'email alredy exist')

class editUser(forms.ModelForm):
    class Meta:
        model = upUserModel
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        data = User.objects.get(id=userId)

        if password1 != password2:
            self.add_error('password2', 'password did not match')
        
        if data.username != username and User.objects.filter(username=username).exists():
            self.add_error('username', 'username alredy exist')

        if data.email != email and User.objects.filter(email=email).exists():
            self.add_error('email', 'email alredy exist')


def passId(id):
    global userId
    userId = id


        