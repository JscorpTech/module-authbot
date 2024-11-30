from .views import LoginView
from django.urls import path


app_name = "authbot"

urlpatterns = [path("login/", LoginView.as_view(), name="login")]
