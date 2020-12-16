from django.urls import path
from .views import login_view, signup_view, profile_view, logout_view
from django.contrib.auth import views as auth_views

app_name = "user_app"

urlpatterns = [
    path("login", auth_views.LoginView.as_view(template_name="user_app/login.html"), name="login"),
    path("signup", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("yourprofile/", profile_view, name="profile"),

]