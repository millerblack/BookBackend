from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
            path('', views.index, name='index'),
            path('create/', views.create, name='create'),
            path('read/id/<int:book_id>/', views.read_id, name='read_id'),
            path('read/name/<str:book_name>/', views.read_name, name='read_name'),
            path('delete/<int:book_id>/', views.delete, name='delete'),
            path('search/<str:book_name>/', views.search, name='search'),
            ]
