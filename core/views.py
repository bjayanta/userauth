from multiprocessing import context
import django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context = {}
    return render(request, 'core/index.html', context)

@login_required(login_url='users.signin')
def dashboard(request):
    context = {}
    return render(request, 'core/dashboard.html', context)
