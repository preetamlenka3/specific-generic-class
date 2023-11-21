from specific.views import *
from django.urls import path



app_name="specific"

urlpatterns=[
    path('sibu/',sibu,name='sibu'),
    path('dani/',dani,name='dani')
]