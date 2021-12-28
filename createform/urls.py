from . import views
from django.urls import path, include

urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
]
