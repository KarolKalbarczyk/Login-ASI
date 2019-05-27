from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Name', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(label='Name', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    email = forms.CharField(label='email', max_length=100)
