from django.urls import path
from . import views

urlpatterns = [
    path('tweets/', views.tweet),
]
