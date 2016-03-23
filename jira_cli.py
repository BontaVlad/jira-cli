import click

import commands


class Config(object):

    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--verbose', is_flag=True)
@pass_config
def cli(config, verbose):
    """Hello world script"""
    config.verbose = verbose


@cli.command()
@click.option('--string', default='World',
              help='This is the thing is greeted')
@click.option('--repeat', default=1,
              help='How many times should be repeated')
@pass_config
def say(config, string, repeat):
    commands.say(config, string, repeat)
