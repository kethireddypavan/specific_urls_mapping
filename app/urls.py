from django.urls import path
from app.views import *


app_name='pavan'


urlpatterns=[
    path('india/',india,name='india'),
]
    