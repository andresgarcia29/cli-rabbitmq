import os
import pika

def __connect():
    try:
        url_connection = os.environ['URL_AMPQ']
        connection = pika.BlockingConnection(pika.ConnectionParameters(url_connection))
        channel = connection.channel()
        return channel
    except:
        raise NameError('Error to connect')

def sendMessage(exchange, body):
    channel = __connect()
    try:
        channel.basic_publish(
                        exchange=exchange_validator(exchange),
                        routing_key='test',
                        body=b'Test message.'
                    )
        connection.close()
    except:
        raise NameError('Error to send message')

def setUrl(url):
    os.environ['URL_AMPQ'] = url

def exchange_validator(exchange):
    valid_options = ['direct', 'fanout', 'topic', 'exchange']
    if exchange not in valid_options:
        raise NameError('The exchange is not valid')
    return exchange
