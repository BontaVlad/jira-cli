import click

from commands import issue as issue_cmd
from signals import echo

from client import Client


class Config(object):

    def __init__(self):
        # username = click.prompt("Username", type=str)
        # password = click.prompt("Password", type=str, hide_input=True)
        self.verbose = False
        self.log = False
        # self.client = Client(username, password)
        self.client = Client()

pass_config = click.make_pass_decorator(Config, ensure=True)


@echo.connect
@pass_config
def handle_echo_signal(config, **kwargs):
    if config.verbose:
        click.echo(kwargs['msg'])
    elif config.log:
        click.echo('should log - {}'.format(kwargs['msg']))


@click.group()
@click.option('--verbose', is_flag=True,
              help='Describe in words what I am doing')
@click.option('--log', is_flag=True,
              help='Send output to default system log location')
@pass_config
def cli(config, verbose, log):
    """Small experimental jira cli application for managing certain jira task
    from the comfort of the terminal"""
    config.verbose = verbose
    config.log = log


@cli.group()
def issue():
    """Issue related actions.
    Use [command] --help to get more info"""
    pass


@issue.command()
@pass_config
def create(config):
    issue_cmd.create(config.client)


@issue.command()
@click.argument('issue')
@pass_config
def get(config, issue):
    issue_cmd.get(config.client, issue)


@issue.command()
@click.argument('issue')
@pass_config
def delete(config, issue):
    issue_cmd.delete(config.client, issue)


@issue.command()
@click.argument('issue')
@pass_config
def edit(config, issue):
    issue_cmd.edit(config.client, issue)
