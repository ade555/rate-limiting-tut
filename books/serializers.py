from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["author_email"]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author_email']=user.id
        return super().create(validated_data)
