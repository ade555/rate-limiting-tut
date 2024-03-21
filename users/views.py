from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .serializers import UserSerializer, APIKeySerializer
from .models import APIKey

class Signup(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = []

    def post(self, request:Request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"successful",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        response = {
            "message":"failed",
            "info":serializer.errors
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

class GetAPIKey(generics.GenericAPIView):
    serializer_class = APIKeySerializer

    def get(self, request:Request):
        api_key = APIKey.objects.get(user=request.user)
        serializer = self.serializer_class(instance=api_key)
        response = {
            "message":"Successful",
            "data":serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
    def put(self, request:Request):
        api_key = APIKey.objects.get(user=request.user)
        api_key.regenerate_key()
        serializer = self.serializer_class(instance=api_key)
        response = {
            "message":"Successful",
            "data":serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)