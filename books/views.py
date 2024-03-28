from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from users.models import APIKey
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def initial(self, request, *args, **kwargs):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            api_key = kwargs.get('api_key')
            try:
                api_key_obj = APIKey.objects.get(key=api_key)
                if api_key_obj.user == request.user:
                    return super().initial(request, *args, **kwargs)
                else:
                    return Response(data={"message": "error", "info": "invalid api key"}, status=status.HTTP_401_UNAUTHORIZED)
            except APIKey.DoesNotExist:
                return Response(data={"message": "error", "info": "invalid api key"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(data={"message": "error", "info": "unauthenticated user"}, status=status.HTTP_401_UNAUTHORIZED)