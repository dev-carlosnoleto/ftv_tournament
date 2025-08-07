from django.db import models

class Mananager(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome Completo") 
    nickname = models.CharField(max_length=255, verbose_name="Apelido")
    phone = models.CharField(max_length=20, verbose_name="Número de celular")
    address = models.CharField(max_length=255, verbose_name="Edereço")
    email = models.CharField(max_length=255, verbose_name="Email")