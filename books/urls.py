from django.urls import path
from .views import BookListCreate

urlpatterns = [
    path('<str:api_key>/', BookListCreate.as_view(), name='book-list-create'),
]
