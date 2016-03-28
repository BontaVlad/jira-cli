import logging

from commands import issue as issue_cmd
from signals import echo
from config import pass_config

import click

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler

handler = logging.FileHandler('jira.log')
handler.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger

logger.addHandler(handler)


@echo.connect
@pass_config
def handle_echo_signal(config, **kwargs):
    if config.verbose:
        click.echo(kwargs['msg'])
    elif config.log:
        logger.info(kwargs['msg'])


@click.group()
@click.option('--verbose', is_flag=True,
              help='Describe in words what I am doing')
@click.option('--log', is_flag=True,
              help='Send output to jira.log')
@pass_config
def cli(config, verbose, log):
    """Small experimental jira cli application for managing certain jira task
    from the comfort of the terminal"""
    config.verbose = verbose
    config.log = log


@cli.command()
@pass_config
def setup(config):
    config.setup()


@cli.group()
def issue():
    """Issue related actions.
    Use [command] --help to get more info"""
    pass


@issue.command()
def create():
    issue_cmd.create()


@issue.command()
@click.argument('issue')
def get(issue):
    issue_cmd.get(issue)


@issue.command()
@click.argument('issue')
def delete(issue):
    issue_cmd.delete(issue)


@issue.command()
@click.argument('issue')
def edit(issue):
    issue_cmd.edit(issue)
