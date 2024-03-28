from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from .models import Book
from users.models import APIKey
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []
    authentication_classes = []

    def dispatch(self, request, *args, **kwargs):
        api_key = request.headers.get("Authorization")
        if api_key:
            try:
                api_key_obj = APIKey.objects.get(key=api_key)
                return super().dispatch(request, *args, **kwargs)
            except Exception:
                return JsonResponse({"message": "Unauthorized. Invalid API key"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return JsonResponse({"message": "API key required"}, status=status.HTTP_400_BAD_REQUEST)