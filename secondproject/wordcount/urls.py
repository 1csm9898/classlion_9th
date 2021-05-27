from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name="wc"),
    path('result/',result,name='result'),
]