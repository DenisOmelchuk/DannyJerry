from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='books'),
]