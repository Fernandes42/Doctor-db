from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import Covid_form
from django.conf import settings
from django.shortcuts import redirect
from .db import insert_into_db, retrieve_rows_from_db, retrieve_ages_from_db
from django.views.generic import ListView
from .models import Covid_tb

# Create your views here.
def register(response):
    form = UserCreationForm();
    return render(response, "register/register.html", {"form":form})

def index(request):
    return render(request, "logged_out/home.html")

def viewdb(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    data = retrieve_rows_from_db()
    ages = retrieve_ages_from_db()
    return render(request, "logged_in/viewdb.html", {'data':data, 'ages':ages})

def publish(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
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
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "logged_in/profile.html")

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "logged_in/dashboard.html")

def tableView(request):
    data = Covid_tb.objects.all()
    return render(request, "table.html", locals())
