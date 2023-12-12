import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from main.forms import SignUpForm
from main.models import Profile

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            profile = Profile.objects.get(user = user)
            if(profile.is_admin()):
            # Status login sukses.
                return JsonResponse({
                    "username": user.username,
                    "status": True,
                    "message": "Login sukses!",
                    "logged_in_as" : "Admin"
                    # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
                }, status=200)
            else :
                return JsonResponse({
                    "username": user.username,
                    "status": True,
                    "message": "Login sukses!",
                    "logged_in_as" : "Buyer"
                    # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
                }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    
@csrf_exempt
def register(request):
    if request.method == 'POST':
        # print(request.body)
        data = json.loads(request.body)
        first_name = "blabla"
        username = data["username"]
        password1 = data["password1"]
        password2 = data["password2"]
        user_type = data["role"]
        last_name = "blabla"
        email = "blabla@gmail.com"
        if password1 != password2:
            return JsonResponse({'status': 'failed', 'message': 'Gagal woi'})

        new_user = User.objects.create_user(username = username, password = password1)
        new_profile = Profile.objects.create(user = new_user, first_name = first_name, last_name = last_name, email =email, role = user_type)
        new_profile.save()
        new_user.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
        

    # @csrf_exempt
    # def signup(request):
    #     form = SignUpForm()
    #     if request.method == "POST":
    #         form = SignUpForm(request.POST)

    #         if form.is_valid():
    #             form.save()
    #             role = form.cleaned_data["role"]

    #             if role == 'A':
    #                 messages.success(request, 'You are now an Admin!')
    #             else:
    #                 messages.success(request, 'You are now a Buyer!')
    #             return redirect('main:login')

    #     context = {'form': form}
    #     return render(request, 'signup.html', context)
