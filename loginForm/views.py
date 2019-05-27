from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from .forms import LoginForm

def loginView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
       
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/succes/')
            else:
                # Return an 'invalid login' error message.
                return HttpResponseRedirect('/login/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def succes(request):
    return render(request, 'registration/succes.html')
