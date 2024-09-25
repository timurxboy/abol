from rest_framework import serializers
from apps.main.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookDetailFilterSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)

    class Meta:
        fields = ['id']
