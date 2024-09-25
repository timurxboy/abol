from rest_framework import serializers


class CreateBookSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    author = serializers.CharField(required=True)
    publication_date = serializers.DateField(required=True)
