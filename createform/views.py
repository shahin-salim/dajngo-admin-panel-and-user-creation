from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, loginform
from django.contrib.auth import authenticate

def register(request):
    if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid(): 
        form.save()
        return redirect('/')
    else:
      form = UserRegisterForm()
    return render(request, 'register.html', {'form': form, 'url': '/register'})

def login(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            name = request.POST['username']
            pwd = request.POST['password']

            user = authenticate(username=name, password=pwd)
            if user is not None:
                a = User.objects.get(username=name)
                if a.is_superuser:
                    return redirect('/adminpanel')
                else:
                    return render(request, 'home.html')
            else:
                return render(request, 'login.html', {'form': form, 'err': 'user not found'})

    else:
        form = loginform()
    return render(request, 'login.html', {'form': form})

