from django.urls import path
from accounts import views

urlpatterns = [
    path('choice-register', views.choice_register, name="choice_register"),
    path('register/manager', views.register_manager, name="register_manager"),
    path('register/player', views.register_player, name="register_player"),
    path('login', views.login, name='login')
]
