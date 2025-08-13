from django.shortcuts import render, redirect
from managers.models import Manager
from managers.forms import ManagerRegistrationForm
from players.models import Player
from players.forms import PlayerRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

def choice_register(request):
    return render(request, 'accounts/choice_register.html')

def register_manager(request):
    if request.method == "POST":
        form = ManagerRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
                email=form.cleaned_data["email"],
                first_name=form.cleaned_data["name"], 
            )

            Manager.objects.create(
                user=user,
                name=form.cleaned_data["name"],
                nickname=form.cleaned_data["nickname"],
                phone=form.cleaned_data["phone"],
                address=form.cleaned_data["address"],
                email=form.cleaned_data["email"],
            )

            messages.success(request, "Conta criada com sucesso!")
            return redirect("login")  
    else:
        form = ManagerRegistrationForm()

    return render(request, "accounts/register_manager.html", {"form": form})

def register_player(request):
    if request.method == "POST":
        form = PlayerRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
                email=form.cleaned_data["email"],
                first_name=form.cleaned_data["name"],
            )

            Player.objects.create(
                user=user,
                name=form.cleaned_data["name"],
                nickname=form.cleaned_data["nickname"],
                phone=form.cleaned_data["phone"],
                address=form.cleaned_data["address"],
                email=form.cleaned_data["email"],
                height=form.cleaned_data["height"],
                weight=form.cleaned_data["weight"],
                age=form.cleaned_data["age"],
            )

            messages.success(request, "Conta criada com sucesso!")
            return redirect("login")
    else:
        form = PlayerRegistrationForm()

    return render(request, "accounts/register_player.html", {"form": form})


def login(request):
    return render(request, 'accounts/login.html')