def __connect():
    try:
        url = os.environ['URL_AMPQ']
        connection = pika.BlockingConnection()
        channel = connection.channel()
        return channel
    except:
        raise NameError('Error to connect')

def sendMessage(body):
    channel = __connect()
    try:
        channel.basic_publish(exchange='direct', routing_key='test',
                        body=b'Test message.')
        connection.close()
    except:
        raise NameError('Error to send message')

def setUrl(url):
    os.environ['URL_AMPQ'] = url
