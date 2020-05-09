from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import Covid_form
from .db import insert_into_db, retrieve_from_db

# Create your views here.
def register(response):
    form = UserCreationForm();
    return render(response, "register/register.html", {"form":form})

def index(request):
    return render(request, "logged_out/home.html")

def viewdb(request):
    data = retrieve_from_db()
    return render(request, "logged_in/viewdb.html", {'data':data})

def publish(request):
    if request.method == 'POST':
        form = Covid_form(request.POST)
        if form.is_valid():
            dict = form.cleaned_data
            print(dict)
            insert_into_db(dict)
    else:
        form = Covid_form
        print(form)
    return render(request, 'logged_in/publish.html', {'form': form})

def profile(request):
    return render(request, "logged_in/profile.html")

def dashboard(request):
    return render(request, "logged_in/dashboard.html")
