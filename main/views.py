from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm
from .models import Profile
import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def show_landing_page(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "landingpage.html", context)

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            role = form.cleaned_data["role"]
            if role == 'S':
                messages.success(request, 'You are now a Seller!')
            else:
                messages.success(request, 'You are now a Buyer!')
            return redirect('main:login')

    context = {'form': form}
    return render(request, 'signup.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)