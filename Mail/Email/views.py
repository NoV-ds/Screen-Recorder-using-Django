from django.shortcuts import render
from .models import UserDetails
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from Mail.settings import EMAIL_HOST_USER
# Create your views here.

def index(request):
    return render(request, 'login.html')

def SignUp(request):
    if request.method == 'POST':

        full_name = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        user = UserDetails.objects.create(email =email, password = password, fullname = full_name )
        if user:
            mail(email, password)
        return render(request, 'login.html')
    return render(request, 'signup.html')

def mail(email, password):
    Receiver = email
    Subject = "Registration Successful"
    Message = "Welcome to Seize The Ade \n\nYour Registration is Successful\n\nUsername: {}\nPassword: {}".format(email, password)
    return send_mail(Subject, Message, EMAIL_HOST_USER, [Receiver], fail_silently=False,)