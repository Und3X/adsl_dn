from django.urls import path
from . import views as dashboard

urlpatterns = [
    path('', dashboard.index),
]