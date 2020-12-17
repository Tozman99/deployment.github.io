from django.urls import path, reverse
from .views import signup_view, profile_view, logout_view
from django.contrib.auth import views as auth_views

app_name = "user_app"

urlpatterns = [
    path("users/yourprofile/", profile_view, name="profile"),
    path("login/", auth_views.LoginView.as_view(template_name="user_app/login.html"), name="login"),
    path("signup", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),

]