from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'core/index.html', context)

def dashboard(request):
    context = {}
    return render(request, 'core/dashboard.html', context)
