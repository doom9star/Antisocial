from django.urls import path
from .views import vLogin, vRegister

urlpatterns = [
	path("login", vLogin, name="login"),
	path("register", vRegister, name="register"),
]