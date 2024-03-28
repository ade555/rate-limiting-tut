from django.urls import path
from .views import BookListCreate

urlpatterns = [
    path('', BookListCreate.as_view(), name='book-list-create'),
]
