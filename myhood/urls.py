from django.urls import path
from knox import views as knox_views
from .api import RegistrationAPI, LoginAPI, UserAPI
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('user/', UserAPI.as_view()),
]