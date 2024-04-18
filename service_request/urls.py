from django.urls import path
from .views import *


app_name = 'service_request'
urlpatterns = [
    path('', home, name='home'),
    path('create/', service_request_create, name='create')
]