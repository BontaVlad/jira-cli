import os
import logging

import click
try:
    import ConfigParser as configparser
except ImportError:
    import configparser

from commands import issue as issue_cmd
from signals import echo


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


APP_NAME = 'jira-cli'


def read_config():
    cfg = os.path.join(click.get_app_dir(APP_NAME), 'config.ini')
    parser = configparser.RawConfigParser()
    parser.read([cfg])
    rv = {}
    for section in parser.sections():
        for key, value in parser.items(section):
            rv['%s.%s' % (section, key)] = value
    return rv


class Config(object):

    def __init__(self):
        config = read_config()
        if not config:
            if click.confirm('Seems that you dont have a config file, do you'
                             ' want me to create one for you?'):
                click.echo('Well done!')
        self.verbose = False
        self.log = False

pass_config = click.make_pass_decorator(Config, ensure=True)


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


@cli.group()
def issue():
    """Issue related actions.
    Use [command] --help to get more info"""
    pass


@issue.command()
@pass_config
def create(config):
    issue_cmd.create()


@issue.command()
@click.argument('issue')
@pass_config
def get(config, issue):
    issue_cmd.get(issue)


@issue.command()
@click.argument('issue')
@pass_config
def delete(config, issue):
    issue_cmd.delete(issue)


@issue.command()
@click.argument('issue')
@pass_config
def edit(config, issue):
    issue_cmd.edit(issue)
