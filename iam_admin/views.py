from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from createform.forms import UserRegisterForm
from .forms import updateUser, editUser

# Create your views here.

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
        # id = request.POST['id']
        # data = User.objects.get(id=id)

        # data.first_name = request.POST['first_name']
        # data.last_name = request.POST['last_name']
        # data.username = request.POST['username']
        # data.email = request.POST['email']
        # if request.POST['password1'].strip():
        #     data.password = request.POST['password1']
        # data.save()

        f = editUser(request.POST)
        if f.is_valid():
            pass
            return redirect('/adminpanel')

    else:
        f = editUser()
        # id = request.GET['id']
        # data = User.objects.get(id=id)
    return render(request, 'update.html', {'form': f})

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





