import os
import click
import pika

@click.group()
def cli():
    pass

@click.command()
@click.option('--exchange', '-e', default='direct', type=str, help='Choose the exchange.')
@click.option('--queue', '-q', default='', type=str, help='Choose the queue name.')
@click.option('--file', '-f', default='', type=str, help='Choose the json file.')
@click.option('--manually', '-m', is_flag=True, default=False, type=bool, help='Write manually.')
def send(exchange, queue, file, manually):
    """Sending a message to rabbitMQ Message"""
    click.echo('rabbit %s!' % os.environ['MESSAGE'])

cli.add_command(send)

if __name__ == '__main__':
    cli()
