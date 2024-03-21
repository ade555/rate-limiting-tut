from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .serializers import UserSerializer

class Signup(generics.GenericAPIView):
    serializer_class = UserSerializer

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