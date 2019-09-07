import os
import json
import pika
from db import save_queue, get_queue_json, update_queue

def send_message(exchange, queue, file, save, manually):
    channel = __connect()
    __verify_if_queue_exists(channel, queue)
    body = __option_input_logic(queue, file, save, manually)
    try:
        channel.basic_publish(
                        exchange=__exchange_validator(exchange),
                        routing_key=queue,
                        properties=pika.BasicProperties(delivery_mode = 2),
                        body=body
                    )
        channel.close()
    except:
        raise NameError('Error to send message')

def __connect():
    try:
        url_connection = os.environ['URL_AMPQ']
        connection = pika.BlockingConnection(pika.URLParameters(url_connection))
        channel = connection.channel()
        return channel
    except:
        raise NameError('Error to connect')

def __verify_if_queue_exists(channel, queue):
    try:
        channel.queue_declare(
            queue=queue,
            passive=False,
            durable=True,
            exclusive=False,
            auto_delete=False
        )
    except:
        raise NameError('Error to declare queue')

def __save(queue, body):
    save_queue(queue, body)

def __update(queue, body):
    update_queue(queue, body)

def __build_body_manually(body):
    body = json.loads(body)
    keys = body.keys()
    for key in keys:
        body[key] = input('Value for [{0}]: '.format(key))
    return json.dumps(body)

def __option_input_logic(queue, file, save, manually):
    if file:
        body = json.dumps(json.loads(open(file, 'r').read()))
        if save:
            __save(queue, body)
    else:
        body = get_queue_json(queue)
        if manually:
            body = __build_body_manually(body)
        if save:
            __update(queue, body)
    return body

def __exchange_validator(exchange):
    normal_options = ['', 'direct', 'fanout', 'topic', 'exchange']
    if exchange in normal_options:
        return 'amq.{0}'.format(exchange)
    return exchange
