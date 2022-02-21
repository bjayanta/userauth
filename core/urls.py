from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='website.index'),
    path('dashboard/', views.dashboard, name='website.dashboard'),
]