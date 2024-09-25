from __future__ import print_function

import os
import grpc
import book_pb2
import book_pb2_grpc

channel = grpc.insecure_channel(f"{os.getenv('GRPC_SERVER_HOST')}:{os.getenv('GRPC_SERVER_PORT')}")
stub = book_pb2_grpc.BookStub(channel)


def get_book(id):
    return stub.GetBook(book_pb2.BookIdRequest(id=id))


def list_book():
    return stub.ListBook(book_pb2.Empty())


def create_book(name, author: str, publication_date: str):
    return stub.CreateBook(book_pb2.BookResponse(name=name, author=author, publication_date=publication_date))


def update_book(id, name: str, author: str, publication_date: str):
    return stub.UpdateBook(book_pb2.BookResponseID(id=id, name=name, author=author, publication_date=publication_date))


def delete_book(id):
    return stub.DeleteBook(book_pb2.BookIdRequest(id=id))
