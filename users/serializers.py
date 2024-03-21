from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    class Meta:
        model = User
        fields = ["id", 'first_name', 'last_name', 'email', 'username', "password"]

    def create(self, validated_data):
        user= super().create(validated_data)
        password = validated_data['password']
        user.set_password(password)
        user.save()
        return user
