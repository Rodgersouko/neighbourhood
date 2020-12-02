from django.urls import path
from .api import RegistrationAPI
from knox import views as knox_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', RegistrationAPI.as_view()),
]