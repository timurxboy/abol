import datetime
from apps.main.services.rabbitmq import send

import grpc
import book_pb2
import book_pb2_grpc
from apps.main.models import Book as BookModel


class Book(book_pb2_grpc.BookServicer):
    def GetBook(self, request, context):
        try:
            book = BookModel.objects.get(id=request.id)
            return book_pb2.BookResponseID(
                id=book.id, name=book.name, author=book.author,
                publication_date=str(book.publication_date)
            )
        
        except BookModel.DoesNotExist:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Book with ID {request.id} not found.")
            return book_pb2.BookResponseID()

        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal error: {str(e)}")
            return book_pb2.BookResponseID()

    def ListBook(self, request, context):
        books = BookModel.objects.all()
        datas = []
        for book in books:
            datas.append(book_pb2.BookResponseID(
                id=book.id,
                name=book.name,
                author=book.author,
                publication_date=str(book.publication_date)
            ))
        return book_pb2.ListBookResponse(data=datas)

    def CreateBook(self, request, context):
        try:
            book = BookModel.objects.create(
                name=request.name,
                author=request.author,
                publication_date=datetime.datetime.strptime(request.publication_date, '%Y-%m-%d')
            )

            send.send_message(
                f'action:CREATE, ID:{book.id}, name:{book.name} author:{book.author} publication_date:{str(book.publication_date)}'
            )

            return book_pb2.BookResponseID(
                id=book.id, name=book.name, author=book.author,
                publication_date=str(book.publication_date)
            )

        except Exception as _:
            context.set_code(grpc.StatusCode.INTERNAL)
            return book_pb2.BookResponseID()

    def UpdateBook(self, request, context):
        try:
            book = BookModel.objects.get(id=request.id)
            book.name = request.name
            book.author = request.author
            book.publication_date = datetime.datetime.strptime(request.publication_date, '%Y-%m-%d')
            book.save()

            send.send_message(
                f'action:UPDATE, ID:{book.id}, name:{book.name} author:{book.author} publication_date:{str(book.publication_date)}'
            )

            return book_pb2.BookResponseID(
                id=book.id, name=book.name, author=book.author,
                publication_date=str(book.publication_date)
            )

        except BookModel.DoesNotExist:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Book with ID {request.id} not found.")
            return book_pb2.BookResponseID()

        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal error: {str(e)}")
            return book_pb2.BookResponseID()

    def DeleteBook(self, request, context):
        try:
            book = BookModel.objects.get(id=request.id)
            book.delete()

            send.send_message(
                f'action:DELETE, ID:{request.id}, name:{book.name} author:{book.author} publication_date:{str(book.publication_date)}'
            )

            return book_pb2.Empty()

        except BookModel.DoesNotExist:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Book with ID {request.id} not found.")
            return book_pb2.Empty()

        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal error: {str(e)}")
            return book_pb2.Empty()
