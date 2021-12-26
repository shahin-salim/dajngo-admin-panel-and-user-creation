from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from createform.forms import UserRegisterForm

# Create your views here.

def home(request):
    data = User.objects.all()
    return render(request, 'panel.html', {'data': data})

def update(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            pass

    else:
        form = UserRegisterForm()
        data = User.objects.get(id=request.GET['id'])
    return render(request, 'register.html', {'url':'/adminpanel/update', 'form': form, 'is_update': True, 'data': data})


def delete(request):
    pass

