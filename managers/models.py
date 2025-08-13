from django.db import models
from django.contrib.auth.models import User

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="manager_profile")
    name = models.CharField(max_length=255, verbose_name="Nome Completo") 
    nickname = models.CharField(max_length=255, verbose_name="Apelido")
    phone = models.CharField(max_length=20, verbose_name="Número de celular")
    address = models.CharField(max_length=255, verbose_name="Endereço")
    email = models.CharField(max_length=255, verbose_name="Email")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nickname or self.name