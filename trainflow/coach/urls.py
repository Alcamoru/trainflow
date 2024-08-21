from django.urls import path

from .views import *

urlpatterns = [
    path('coach', coach, name='coach'),
    path('calendar', calendar, name='calendar'),
]
