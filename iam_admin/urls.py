
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('/update', views.update, name='update'),
    path('/delete', views.delete, name='delete'),
    path('/logout', views.logout, name='logout'),
    path('/createuser', views.createuser, name='logout'),
]
