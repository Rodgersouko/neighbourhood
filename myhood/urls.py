from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
]