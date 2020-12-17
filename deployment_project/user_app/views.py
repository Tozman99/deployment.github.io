from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .forms import User_form
from django.http import HttpResponseRedirect

# Create your views here.




def signup_view(request):

    form = User_form()

    if request.method == "POST":
        form = User_form(request.POST)

        if form.is_valid():

            form.save()
            
            return HttpResponseRedirect("users/login")

        return render(request, "user_app/signup.html", {"form":form})

    return render(request, "user_app/signup.html", {"form": form})



def profile_view(request):

    obj = User.objects.get(username=request.user.username)

    return render(request, "user_app/profile.html", {"person":obj})

def logout_view(request):

    return render(request, "user_app/logout.html", {})