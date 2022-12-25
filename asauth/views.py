from django.shortcuts import render
from .forms import LoginForm, RegisterForm

def vLogin(req):
	return render(req, 'asauth/login.html', {"form": LoginForm()})

def vRegister(req):
	return render(req, 'asauth/register.html', {"form": RegisterForm()})