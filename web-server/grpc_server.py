import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from concurrent import futures
import logging

import grpc
import book_pb2_grpc
from apps.main.services.grpc_handlers.BookService import Book


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_BookServicer_to_server(Book(), server)
    server.add_insecure_port("[::]:" + os.getenv('GRPC_SERVER_PORT'))
    server.start()
    print("Server started, listening on " + os.getenv('GRPC_SERVER_PORT'))
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
