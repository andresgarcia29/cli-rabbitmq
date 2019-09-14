import os
import click
import pika
from rabbit import send_message
from rabbit import listener_queue
from db import start_database

@click.group()
def cli():
    pass

@click.command()
@click.option('--exchange', '-e', default='direct', type=str, help='Choose the exchange.')
@click.option('--queue', '-q', default='', type=str, help='Choose the queue name.')
@click.option('--file', '-f', default='', type=str, help='Choose the json file.')
@click.option('--save', '-s', is_flag=True, default=False, type=bool, help='Save the json file.')
@click.option('--manually', '-m', is_flag=True, default=False, type=bool, help='Write manually.')
@click.option('--counter', '-c', default=1, type=int, help='Repeat # times.')
def send(exchange, queue, file, save, manually, counter):
    """Sending a message to rabbitMQ Message"""
    for _ in range(0, counter):
        send_message(exchange, queue, file, save, manually)

@click.command()
@click.option('--queue', '-q', default='', type=str, help='Choose the queue name.')
@click.option('--auto', '-a', is_flag=True, default=False, type=bool, help='Select Auto Ack.')
def listener(queue, auto):
    """Listen a rabbitmq queue and show the body"""
    listener_queue(queue, auto)

cli.add_command(send)
cli.add_command(listener)

if __name__ == '__main__':
    start_database()
    cli()
