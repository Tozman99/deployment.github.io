from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import User_form, Profile_form

# Create your views here.


def login_view(request):


    return render(request, "user_app/login.html", {})



def signup_view(request):

    return render(request, "user_app/signup.html", {})



def profile_view(request):

    return render(request, "user_app/login.html", {})

def logout_view(request):

    return render(request, "user_app/logout.html", {})