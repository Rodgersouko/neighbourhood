from django.urls import path, include
from knox import views as knox_views
from . import views
from .views import RegisterAPI,LoginAPI,ChangePasswordView           

urlpatterns = [
    # path('register/', RegisterAPI.as_view(), name='register'),
    # path('login/', LoginAPI.as_view(), name='login'),
    # path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    # path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    # path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    #path('api/profile/', Profile.as_view(), name='profile'),

    path('', views.home, name='home'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    
]