from django.urls import path
from accounts import views

urlpatterns = [
    path('choice-register', views.choice_register, name="choice_register"),
    path('register/manager', views.register_manager, name="register_manager"),
    path('login', views.login, name='login')
]
