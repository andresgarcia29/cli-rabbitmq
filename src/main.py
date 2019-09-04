import os
import click
import pika
from rabbit import setUrl, sendMessage

@click.group()
def cli():
    pass

@click.command()
@click.option('--url', '-u', default='', type=str, help='Url to connect with RabbitMq')
def connect(url):
    """Set the rabbitmq url to know where connect"""
    setUrl(url)

@click.command()
@click.option('--exchange', '-e', default='direct', type=str, help='Choose the exchange.')
@click.option('--queue', '-q', default='', type=str, help='Choose the queue name.')
@click.option('--file', '-f', default='', type=str, help='Choose the json file.')
@click.option('--save', '-s', default='', type=str, help='Save the json file.')
@click.option('--manually', '-m', is_flag=True, default=False, type=bool, help='Write manually.')
@click.option('--counter', '-c', default=1, type=int, help='Repeat # times')
def send(exchange, queue, file, save, manually, counter):
    """Sending a message to rabbitMQ Message"""
    for _ in range(0, counter):
        sendMessage(exchange, queue, file, save, manually)

cli.add_command(send)

if __name__ == '__main__':
    cli()