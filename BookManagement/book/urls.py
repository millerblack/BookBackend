from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
            path('', views.index, name='index'),
            path('create', views.create, name='create'),
            path('read/<int:book_id>/', views.read, name='read'),
            path('delete', views.delete, name='delete'),
            path('search', views.search, name='search'),
            ]
