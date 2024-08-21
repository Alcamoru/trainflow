from django.urls import path

from .views import index, building

urlpatterns = [
    path('', index, name='index'),
    path("building", building, name='building'),
]
