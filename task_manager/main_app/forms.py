

from django import forms
from .models import Task
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Введите ваш пароль'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'placeholder': 'Введите ваш пароль повторно'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Введите вашу почту'}),
            'first_name' : forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
            'username': forms.TextInput(attrs={'placeholder': 'Введите ваш никнейм'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'date_finish', 'color', 'text']
        widgets = {
            'date_finish': forms.DateInput(attrs={'type': 'date'}),
            'color': forms.NumberInput(attrs={'step': '1','min': '0', 'max': '5'}),
        }

