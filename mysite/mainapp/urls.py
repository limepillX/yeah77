from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('list', list_data, name='list'),
]