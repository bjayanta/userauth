from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name="users.signin"),
    path('registration/', views.registration, name="users.registration"),
    path('signout/', views.signout, name="users.signout"),
]
