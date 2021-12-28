from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, loginform
from django.contrib.auth import authenticate
from django.views.decorators.cache import never_cache

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
    if 'user' in request.session:
        return redirect('/home')
    if request.method == 'POST':
        
        form = loginform(request.POST)
        if form.is_valid():

            name = request.POST['username']
            pwd = request.POST['password']

            user = authenticate(username=name, password=pwd)
            if user is not None:
                a = User.objects.get(username=name)
                if a.is_superuser:
                    request.session['admin'] = request.POST['username']
                    return redirect('/adminpanel')
                else:
                    request.session['user'] = request.POST['username']
                    return redirect('/home')
            else:
                return render(request, 'login.html', {'form': form, 'err': 'user not found'})

    else:
        form = loginform()
    return render(request, 'login.html', {'form': form})

@never_cache
def home(request):
    if request.session.has_key('user'):
        return render(request, 'home.html')
    return redirect('/')

def logout(request):
    if request.session.has_key('user'):
        del request.session['user']
    return redirect('/')
