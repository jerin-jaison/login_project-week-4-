from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginn, name='login'),
    path('home', views.home, name='home'),
    path('signout', views.signout, name='signout'),
]
