#!/usr/bin/env python

import click
from lib.calculator import add, subtract, multiply, divide


@click.group()
def cli():
    """CLI Calculator"""


@cli.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_cmd(a, b):
    """Add two numbers"""
    click.echo(add(a, b))


@cli.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def sub(a, b):
    """Subtract two numbers"""
    click.echo(subtract(a, b))


@cli.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def mul(a, b):
    """Multiply two numbers"""
    click.echo(multiply(a, b))


@cli.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def div(a, b):
    """Divide two numbers"""
    try:
        result = divide(a, b)
        click.echo(result)
    except ValueError as e:
        click.echo(str(e))


if __name__ == "__main__":
    cli()
