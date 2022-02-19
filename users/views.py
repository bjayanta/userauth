from django.shortcuts import render
from .forms import SignUpForm, UserCreationForm
from django.contrib import messages

# Create your views here.
def registration(request):
    form = SignUpForm(request.POST)

    if form.is_valid:
        pass
    else:
        form = SignUpForm()

    context = {
        "form": form
    }

    return render(request, 'users/registration.html', context)
