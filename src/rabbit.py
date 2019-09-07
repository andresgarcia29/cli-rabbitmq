import os
import json
import pika

def __connect():
    try:
        url_connection = os.environ['URL_AMPQ']
        connection = pika.BlockingConnection(pika.URLParameters(url_connection))
        channel = connection.channel()
        return channel
    except:
        raise NameError('Error to connect')

def __save(file):
    pass

def sendMessage(exchange, queue, file, save, manually):
    channel = __connect()
    
    if save:
        __save(file)
    else:
        body = json.dumps(open(file, 'r').read())

    try:
        channel.basic_publish(
                        exchange=exchange_validator(exchange),
                        routing_key=queue,
                        body=body
                    )
        channel.close()
    except:
        raise NameError('Error to send message')

def exchange_validator(exchange):
    valid_options = ['', 'direct', 'fanout', 'topic', 'exchange']
    if exchange not in valid_options:
        raise NameError('The exchange is not valid')
    return 'amq.{0}'.format(exchange)
