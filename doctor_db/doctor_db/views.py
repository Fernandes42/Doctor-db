from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, "home.html")
def accessdb(request):
    return render(request, "accessdb.html")
def register(response):
    form = UserCreationForm();
    return render(response, "register/register.html", {"form":form})
