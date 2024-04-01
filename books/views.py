from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.http import JsonResponse

from .models import Book
from users.models import APIKey
from .serializers import BookSerializer

class CustomAPIView(generics.GenericAPIView):
    permission_classes = []
    authentication_classes = []

    def dispatch(self, request, *args, **kwargs):
        api_key = request.headers.get("Authorization")
        if api_key:
            try:
                api_key_obj = APIKey.objects.get(key=api_key)
                return super().dispatch(request, *args, **kwargs)
            except Exception as e:
                print(str(e))
                return JsonResponse({"message": "Unauthorized. Invalid API key"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return JsonResponse({"message": "API key required"}, status=status.HTTP_400_BAD_REQUEST)

class BookListCreate(CustomAPIView):
    serializer_class = BookSerializer

    def get(self, request:Request):

        api_key = request.headers.get("Authorization")
        api_key_obj = APIKey.objects.get(key=api_key)

        queryset = Book.objects.filter(author_email=api_key_obj.user)
        serializer = self.serializer_class(instance=queryset, many=True)
        response = {
             "message":"successful",
             "data": serializer.data
         }
        return Response(data=response, status=status.HTTP_200_OK)
    
    def post(self, request:Request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            response = {
             "message":"successful",
             "data": serializer.data
             }
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        response = {
             "message":"Failed",
             "info": serializer.errors
             }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
