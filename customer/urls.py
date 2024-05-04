from django.urls import path
from .views import *

app_name = 'customer'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
]