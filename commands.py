import click


def say(config, string, repeat):
    click.echo(config.verbose)
    for x in xrange(repeat):
        click.echo(string)
