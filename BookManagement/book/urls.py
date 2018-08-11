from django.urls import path
from . import views

urlpatterns = [
            path('create', views.create, name='create'),
            path('read', views.read, name='read'),
            path('delete', views.delete, name='delete'),
            path('search', views.search, name='search'),
            ]
