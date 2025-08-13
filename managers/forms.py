from django import forms
from django.contrib.auth.models import User
from .models import Manager

class ManagerRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, label="Usuário")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmar Senha")

    name = forms.CharField(max_length=255, label="Nome Completo")
    nickname = forms.CharField(max_length=255, label="Apelido")
    phone = forms.CharField(max_length=20, label="Número de celular")
    address = forms.CharField(max_length=255, label="Endereço")
    email = forms.EmailField(max_length=255, label="Email")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("password_confirm")
        if password != confirm:
            self.add_error("password_confirm", "As senhas não coincidem.")
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})