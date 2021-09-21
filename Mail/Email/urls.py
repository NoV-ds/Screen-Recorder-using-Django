from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Login'),
    path('signup/', views.SignUp, name='SignUp'),
]