from django.urls import path, include
from .views import *

urlpatterns = [
    path('', test, name='main'),
    path('hashes/', hashes, name='hashes'),
    path('read/', read, name='read'),
    path('write/', write, name='write'),
    path('show/<str:filename>', show, name='show'),
    path('show_parsed/<str:filename>', show_parsed, name='show_parsed'),
    path('show/', show, name='show'),
]

