from django.urls import path
from accounts import views

urlpatterns = [
    path('choice-register', views.choice_register, name="choice_register"),
    path('register/manager', views.render_register_manager, name="render_register_manager"),
    path('register/player', views.render_register_player, name="render_register_player"),
]
