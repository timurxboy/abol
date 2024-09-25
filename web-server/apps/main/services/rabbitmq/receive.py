import pika
import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s | %(asctime)s | %(filename)s | %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def callback(ch, method, properties, body):
    logger.info(body)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv('RABBITMQ_HOST')))
    channel = connection.channel()

    channel.queue_declare(queue='book')

    channel.basic_consume(queue='book', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == "__main__":
    main()
