# -*- coding: utf-8 -*-

"""Command line interface for ``iter-together``.

Why does this file exist, and why not put this in ``__main__``? You might be tempted to import things from
`__main__`` later, but that will cause problems--the code will get executed twice:

- When you run ``python3 -m iter_together`` python will execute``__main__.py`` as a script. That means there won't be
  any ``iter_together.__main__`` in ``sys.modules``.
- When you import __main__ it will get executed again (as a module) because
  there's no ``iter_together.__main__`` in ``sys.modules``.

.. seealso:: http://click.pocoo.org/7/setuptools/#setuptools-integration
"""

import click

from .utils import iter_together

__all__ = [
    'main',
]


@click.command()
@click.argument('left', type=click.Path(file_okay=True, dir_okay=False))
@click.argument('right', type=click.Path(file_okay=True, dir_okay=False))
@click.option('-s', '--sep', default=',', show_default=True)
def main(left: str, right: str, sep: str):
    """Iterate two files together."""
    for line in iter_together(left, right):
        click.echo(sep.join(line))


if __name__ == '__main__':
    main()
