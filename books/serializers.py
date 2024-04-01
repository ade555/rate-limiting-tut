from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["id", "author", "publication_date"]

    def create(self, validated_data):
        author = self.context['api_key'].user
        validated_data['author']=author
        return super().create(validated_data)
