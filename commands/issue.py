import click
from signals import echo


def create(client):
    echo.send(msg='creating issue')
    echo.send(msg='result')


def get(client, issue):
    click.echo('retriving issue - {}'.format(issue))


def delete(client, issue):
    click.echo('deleting issue - {}'.format(issue))


def edit(client, issue):
    click.echo('edit issue - {}'.format(issue))
