from dataclasses import field
from django import forms
from .models import *
from django.forms import EmailInput, ModelForm, NumberInput, TextInput, DateTimeInput, Textarea


class Logreg(forms.ModelForm):
    class Meta:
        model = regis
        fields = ['username', 'email', 'password', 'confirm']


class UsersLog(forms.ModelForm):
    class Meta:
        model = regis
        fields = ['username', 'password']



class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeHolder': ' name of post'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeHolder': ' Anons'
            }),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeHolder': ' Text'

            }),
        }