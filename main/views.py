from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SignUpForm
from .models import Profile

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
            return redirect('main:login_user')

    context = {'form': form}
    return render(request, 'signup.html', context)
