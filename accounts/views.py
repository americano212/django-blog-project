from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from .models import Account
# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
        else:
            pass
    return render(request,"accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("accounts:login")


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        name = request.POST["name"]
        nickname = request.POST["nickname"]
        phone_num = request.POST["phone_num"]
        birth_y = request.POST["birth_y"]
        birth_m = request.POST["birth_m"]
        birth_d = request.POST["birth_d"]
        id_boj = request.POST["id_boj"]
        id_cf = request.POST["id_cf"]
        id_github = request.POST["id_github"]

        user = Account.objects.create_user(username,email,password)
        user.name = name
        user.nickname = nickname
        user.phone_num = phone_num
        user.birth_y = birth_y
        user.birth_m = birth_m
        user.birth_d = birth_d
        user.id_boj = id_boj
        user.id_cf = id_cf
        user.id_github = id_github
        user.save()
        return redirect("accounts:login")

    return render(request,"accounts/signup.html")
