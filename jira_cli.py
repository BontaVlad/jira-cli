import click

from commands import issue as issue_cmd

from client import Client


class Config(object):

    def __init__(self):
        username = click.prompt("Username", type=str)
        password = click.prompt("Password", type=str, hide_input=True)
        self.verbose = False
        self.client = Client(username, password)

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--verbose', is_flag=True)
@pass_config
def cli(config, verbose):
    """Hello world script"""
    config.verbose = verbose


@cli.group()
def issue():
    """Issue related actions"""
    pass


@issue.command()
@pass_config
def create(config):
    issue_cmd.create(config.client)


@issue.command()
@click.argument('issue_id')
@pass_config
def get(config, issue_id):
    issue_cmd.get(config.client, issue_id)


@issue.command()
@click.argument('issue_id')
@pass_config
def delete(config, issue_id):
    issue_cmd.delete(config.client, issue_id)


@issue.command()
@click.argument('issue_id')
@pass_config
def edit(config, issue_id):
    issue_cmd.edit(config.client, issue_id)
