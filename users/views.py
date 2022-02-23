from email import message
from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import SignUpForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
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
                return redirect('website.dashboard')
    else:
        form = SignUpForm()

    context = {
        "form": form
    }

    return render(request, 'users/registration.html', context)

def signin(request):
    context = {}

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            # redirect to dashboard view
            return redirect('website.dashboard')
        else:
            messages.error(request, "Bad Credentials!")
    
    return render(request, 'users/login.html', context)

def signout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Logged out successfully!")

        return redirect('website.index')
