import pika
import os


def send_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv('RABBITMQ_HOST')))
    channel = connection.channel()

    channel.queue_declare(queue='book')

    channel.basic_publish(exchange='',
                          routing_key='book',
                          body=message)
    connection.close()
