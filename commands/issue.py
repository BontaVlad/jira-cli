import click


def create(client):
    click.echo('creating issue')


def get(client, issue_id):
    click.echo('retriving issue - {}'.format(issue_id))
    res = client.get_issue(issue_id)
    return res


def delete(client, issue_id):
    click.echo('deleting issue - {}'.format(issue_id))


def edit(client, issue_id):
    click.echo('edit issue - {}'.format(issue_id))
