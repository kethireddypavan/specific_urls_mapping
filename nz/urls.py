from django.urls import path
from nz.views import *


app_name='kane'


urlpatterns=[
    path('nz/',nz,name='nz'),
]