from django import forms
from django.db import connection
from abc import ABC, abstractmethod
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Name', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    request = None

    def __init__(self,POST=None,request=None):
        self.request = request
        super().__init__(POST)

    def is_valid(self):
        if not super().is_valid():
            return "Invalid input"
        if self.is_data_base_connected():
            return self.registration_work()
        else:
            return "No database Connection"



    def is_data_base_connected(self):
        try:
            connection.ensure_connection()
            return True
        except Exception:
            return False


    def registration_work(self):
        pass


class LoginForm(RegistrationForm):

    def registration_work(self):
        insertedUsername = self.cleaned_data['username']
        insertedPassword = self.cleaned_data['password']
        user = authenticate(self.request,username= insertedUsername,password= insertedPassword)
        if user is not None:
            login(self.request, user)
            return ""
        else:
            return "Wrong username or password"
        
        

class SignUpForm(RegistrationForm):

    def registration_work(self):
        insertedUsername = self.cleaned_data['username']
        insertedPassword = self.cleaned_data['password']
        try:
            User.objects.create_user(insertedUsername,email='',password= insertedPassword)
            return ''
        except:
            return 'Ta nazwa uzytkownika jest juz zajeta'


        
