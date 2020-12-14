from django.urls import path
from .views import home_view

app_name = "test_app"

urlpatterns = [

    path("", home_view, name="home"),
]
