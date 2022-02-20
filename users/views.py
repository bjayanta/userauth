from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import SignUpForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def registration(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            form.save()

            newUser = authenticate(username=username, password=password)
            if newUser is not None:
                login(request, newUser)
                HttpResponseRedirect('website.index')
    else:
        form = SignUpForm()

    context = {
        "form": form
    }

    return render(request, 'users/registration.html', context)
