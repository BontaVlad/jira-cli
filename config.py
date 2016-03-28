import os

try:
    import ConfigParser as configparser
except ImportError:
    import configparser

import click


APP_NAME = 'jira-cli'
CONFIG_NAME = 'config.ini'


def read_config():
    cfg = os.path.join(click.get_app_dir(APP_NAME), CONFIG_NAME)
    parser = configparser.RawConfigParser()
    parser.read([cfg])
    rv = {}
    for section in parser.sections():
        for key, value in parser.items(section):
            rv['%s.%s' % (section, key)] = value
    return rv


class Config(object):

    def __init__(self):
        self.config = read_config()
        if not self.config:
            if click.confirm('Seems that you dont have a config file, shall we'
                             ' create a config file?'):
                self.setup()

    def setup(self):
        click.echo('Making the setup')


pass_config = click.make_pass_decorator(Config, ensure=True)
