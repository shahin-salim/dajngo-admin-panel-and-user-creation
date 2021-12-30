from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from createform.forms import UserRegisterForm
from .forms import  editUser, passId

@never_cache
def home(request):
    if 'admin' not in request.session:
        return redirect('/')

    elif request.method == 'POST':
        val = request.POST['search']
        data = User.objects.filter(username__icontains=val)
        return render(request, 'panel.html', {'data': data, 'val': val})
            
    data = User.objects.all()
    return render(request, 'panel.html', {'data': data})

@never_cache
def update(request):
    if 'admin' not in request.session:
        return redirect('/')

    if request.method == 'POST':
        id = request.POST['id']
        data = User.objects.get(id=id)
        passId(id)
        f = editUser(request.POST, initial={'first_name': data.first_name, 'last_name': data.last_name, 'username': data.username, 'email': data.email})
        if f.is_valid():
            a =  f.cleaned_data
            data.first_name = a['first_name']
            data.last_name = a['last_name']
            data.username = a['username']
            data.email = a['email']
            if a['password1']:
                data.password = make_password(a['password1'])
            data.save()
            return redirect('/adminpanel')

    else:
        id = request.GET['id']
        data = User.objects.get(id=id)
        f = editUser(initial={'first_name': data.first_name, 'last_name': data.last_name, 'username': data.username, 'email': data.email})

    return render(request, 'update.html', {'form': f, 'id':id})

@never_cache
def delete(request):
    if 'admin' not in request.session:
        return redirect('/')
        
    User.objects.filter(id=request.GET['id']).delete()
    return redirect('/adminpanel')

@never_cache
def logout(request):
    if 'admin' in request.session:
        del request.session['admin']
    return redirect('/')

@never_cache
def createuser(request):
    if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid(): 
        form.save()
        return redirect('/adminpanel')
    else:
      form = UserRegisterForm()
    return render(request, 'register.html', {'form': form, 'url': '/adminpanel/createuser', 'is_createuser': True})
