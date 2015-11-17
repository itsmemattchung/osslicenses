import click
from tabulate import tabulate
import github3


@click.group()
@click.pass_context
def cli(context):
    gh = github3.GitHub()
    licenses = sorted(gh.licenses(), key=str)
    context.obj = {
        'gh': github3.GitHub(),
        'licenses': licenses
    }


@cli.command()
@click.pass_obj
def list(obj):
    """
    List all open source licenses
    """
    licenses = obj['licenses']
    click.echo(tabulate({
        "Key": [license.key for license in licenses],
        "Name": [license.name for license in licenses],
        },
        headers="keys"
    ))


@cli.command()
@click.pass_obj
@click.argument(
    'name',
)
def get(context, name):
    """
    Get a license specified by key
    """
    gh = context['gh']
    license = gh.license(name)
    print license.body
