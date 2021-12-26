from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    data = User.objects.all()
    return render(request, 'panel.html', {'data': data})

def update(request):


    if request.method == 'POST':
        id = request.POST['id']
        row = User.objects.get(id=id)
        row.first_name = request.POST['first_name'].strip()
        row.last_name = request.POST['last_name'].strip()
        row.username = request.POST['username'].strip()
        row.email = request.POST['email'].strip()
        if request.POST['password1'].strip() != '':
            row.password = make_password(request.POST['password1'].strip())
        row.save()
        return redirect('/adminpanel')


    else:
        id = request.GET['id']
        row = User.objects.get(id=id)
        
    return render(request, 'update.html', {'row': row})


def delete(request):
    User.objects.filter(id=request.GET['id']).delete()
    return redirect('/adminpanel')

def block(request):
    ins = User.objects.get(id=request.GET['id'])
    if ins.blockUser:
        ins.blockUser = 0
    else:
        ins.blockUser = 1
    ins.save()
    return redirect('/adminpanel')





