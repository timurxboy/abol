from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import grpc_client
import grpc
import core.settings as settings
from django.core.cache import cache
from apps.main.serializers import CreateBookSerializer

CACHE_TTL = getattr(settings, 'CACHE_TTL', 60 * 15)

class BookView(APIView):
    serializer_class = CreateBookSerializer

    def prepare_book_data(self, book):
        return {
            "id": book.id,
            "name": book.name,
            "author": book.author,
            "publication_date": book.publication_date
        }

    def handle_grpc_error(self, error):
        if error.code() == grpc.StatusCode.NOT_FOUND:
            return Response(error.details(), status=status.HTTP_404_NOT_FOUND)
        return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetBookDetailView(BookView):
    
    @extend_schema(responses={status.HTTP_200_OK: CreateBookSerializer})
    def get(self, request, pk):
        cached_book = cache.get(f'book_{pk}')
        if cached_book:
            return Response(cached_book, status=status.HTTP_200_OK)

        try:
            response = grpc_client.get_book(id=pk)
            data = self.prepare_book_data(response)
            cache.set(f'book_{pk}', data, timeout=CACHE_TTL)
            return Response(data, status=status.HTTP_200_OK)
        except grpc.RpcError as e:
            return self.handle_grpc_error(e)

    def put(self, request, pk):
        filter_serializer = CreateBookSerializer(data=request.data)
        filter_serializer.is_valid(raise_exception=True)

        try:
            response = grpc_client.update_book(
                id=pk,
                name=filter_serializer.validated_data['name'],
                author=filter_serializer.validated_data['author'],
                publication_date=str(filter_serializer.validated_data['publication_date'])
            )
            data = self.prepare_book_data(response)
            cache.delete('books')
            cache.set(f'book_{pk}', data, timeout=CACHE_TTL)
            return Response(data, status=status.HTTP_200_OK)
        except grpc.RpcError as e:
            return self.handle_grpc_error(e)

    def delete(self, request, pk):
        try:
            grpc_client.delete_book(id=pk)
            cache.delete(f'book_{pk}')
            cache.delete('books')
            return Response(status=status.HTTP_204_NO_CONTENT)
        except grpc.RpcError as e:
            return self.handle_grpc_error(e)


class GetBookView(BookView):
    
    @extend_schema(responses={status.HTTP_200_OK: CreateBookSerializer(many=True)})
    def get(self, request):
        cached_books = cache.get('books')
        if cached_books:
            return Response(cached_books, status=status.HTTP_200_OK)

        response = grpc_client.list_book()
        response_data = [self.prepare_book_data(book) for book in response.data]

        cache.set('books', response_data, timeout=CACHE_TTL)
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        filter_serializer = CreateBookSerializer(data=request.data)
        filter_serializer.is_valid(raise_exception=True)

        try:
            response = grpc_client.create_book(
                name=filter_serializer.validated_data['name'],
                author=filter_serializer.validated_data['author'],
                publication_date=str(filter_serializer.validated_data['publication_date'])
            )
            data = self.prepare_book_data(response)
            cache.delete('books')
            cache.set(f'book_{response.id}', data, timeout=CACHE_TTL)

            cached_books = cache.get('books')
            if cached_books is not None:
                cached_books.append(data)
                cache.set('books', cached_books, timeout=CACHE_TTL)

            return Response(data, status=status.HTTP_201_CREATED)
        except grpc.RpcError as e:
            return self.handle_grpc_error(e)
