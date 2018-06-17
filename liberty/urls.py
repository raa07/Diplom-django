from . import views
from django.urls import path

urlpatterns = [
    path(r'', views.book_list, name='book_list'),
    path(r'book/<int:pk>', views.book_detail, name='book_detail'),
]