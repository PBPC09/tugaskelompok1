from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm
from .models import Profile
import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_landing_page(request):
    context = {}
    return render(request, "landingpage.html", context)

@csrf_exempt
def show_landing_page_logged_in(request):
    context = {}
    return render(request, "landingpageafterlogin.html", context)

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            role = form.cleaned_data["role"]

            if role == 'Admin':
                messages.success(request, 'You are now an Admin!')
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
            profile = Profile.objects.get(user=user)
            login(request, user)
            response = None

            if profile.is_admin():
                response = HttpResponseRedirect(reverse("registerbook:show_registered_books"))
            else:
                response = HttpResponseRedirect(reverse("main:show_landing_page_logged_in"))
 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:show_landing_page')