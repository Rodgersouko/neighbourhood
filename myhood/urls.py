from django.urls import path, include
from knox import views as knox_views
from .api import RegistrationAPI, LoginAPI, UserAPI
from . import views
from .views import RegisterAPI, ChangePasswordView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Hoods', views.HoodViewset)

urlpatterns = [
    #path('admin/,admin.viewsite.urls'),
    


    #path('', views.home, name='home'),
    path('register/', RegistrationAPI.as_view(),name='register'),
    path('login/', LoginAPI.as_view(),name='login'),
    path('user/', UserAPI.as_view(),name='user'),
    path('logout/', knox_views.LogoutAllView.as_view(), name='knox_logout'),
    path('logoutall/', RegisterAPI.as_view(), name='logoutall'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
    
# urlpatterns = [
#     path('api/login/', LoginAPI.as_view(), name='login'),
#     path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
#     path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
# ]