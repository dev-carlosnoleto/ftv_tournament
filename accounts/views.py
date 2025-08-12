from django.shortcuts import render, redirect


def choice_register(request):
    return render(request, 'accounts/choice_register.html')

def render_register_manager(request):
    return render(request, 'accounts/register_manager.html')

def render_register_player(request):
    return render(request, 'accounts/register_player.html')