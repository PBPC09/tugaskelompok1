<<<<<<< HEAD
from django.shortcuts import render, redirect
=======
from django.shortcuts import render,redirect
>>>>>>> 6e20312ef3086855cb1a5dba4b0e11c5ccf2df13
from django.contrib import messages
from .forms import SignUpForm
from .models import Profile

<<<<<<< HEAD
# Create your views here.
def show_landing_page(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "landingpage.html", context)

=======
>>>>>>> 6e20312ef3086855cb1a5dba4b0e11c5ccf2df13
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
<<<<<<< HEAD
            return redirect('main:login')

    context = {'form': form}
    return render(request, 'signup.html', context)

=======
            return redirect('main:login_user')

    context = {'form': form}
    return render(request, 'signup.html', context)
>>>>>>> 6e20312ef3086855cb1a5dba4b0e11c5ccf2df13
