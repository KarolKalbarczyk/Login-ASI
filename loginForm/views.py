from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import LoginForm
from .forms import SignUpForm

def loginView(request):
    # if this is a POST request we need to process the form data
    text = ''
    if request.method == 'POST':
        print(request.POST)
        # create a form instance and populate it with data from the request and request itself:
        form = LoginForm(request.POST,request)
        # check whether it's valid:
        text = form.is_valid()
        if len(text) == 0:
            return HttpResponseRedirect('/succes/')
    # if method is GET or there was an error we create blank form
    form = LoginForm()
    return render(request, 'registration/login.html', {'form': form , 'text':text})


def succes(request):
    return render(request, 'registration/succes.html')

def sign_up(request):
    text = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        text = form.is_valid()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form, 'text':text})
