from django.urls import path
from aus.views import *


app_name='aus'


urlpatterns=[
    path('aus/',aus,name='aus'),
]