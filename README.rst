iter-together
=============
Simultaneously iterate over multiple files with the same index column.

This package was written to accompany the tutorial `Reusable, Reproducible, Useful Computational Science in
Python <bit.ly/2ZXoBMA>`_ that was organized by `CoronaWhy <https://github.com/coronawhy/>`_ and presented
by `Charles Tapley Hoyt <https://github.com/cthoyt/>`_ on June 3rd, 2020.

Installation
------------
``iter-together`` can be installed in development mode with:

.. code-block:: sh

    $ git clone https://travis-ci.com/cthoyt-teaches-reproducibility/iter-together-FINISHED.git iter-together
    $ cd iter-together
    $ pip install -e .[docs]

- ``-e`` installs in editable mode
- ``.`` says install the current directory
- ``[docs]`` says install the extra requirements for building the docs

It can also be installed in ready-to-go mode from the latest code on
`GitHub <https://travis-ci.com/cthoyt-teaches-reproducibility/iter-together-FINISHED>`_ with:

.. code-block:: sh

    $ pip install git+https://travis-ci.com/cthoyt-teaches-reproducibility/iter-together-FINISHED.git

Documentation |documentation|
-----------------------------
Documentation is automatically built with every push to master and served by ReadTheDocs at
https://cthoyt-teaches-reproducibility-iter-together-finished.readthedocs.io.

If you want to build the documentation locally after cloning the repository and installing in development mode,
you can do the following to build and open the docs (sorry windows users, you're out of luck):

.. code-block:: sh

    $ cd docs/
    $ make html
    $ open build/html/index.html

Automated Testing |build|
-------------------------
All of the settings for checking package metadata quality (pyroma), package integrity (MANIFEST.in, check-manifest),
code quality (flake8), documentation quality (doc8), running unit tests (pytest), checking code
coverage (codecov; coverage-report) can be run with ``tox`` with the following:

.. code-block:: sh

    $ pip install tox
    $ tox

Later, it automatically gets run by Travis-CI on every push.

Versioning
----------
This project uses semantic versioning (https://semver.org/) that is handled by ``bumpversion``. The configuration
is in ``.bumpversion.cfg``. If you want to bump the version, you can do the following:

.. code-block:: sh

    $ pip install bumpversion
    $ bumpversion patch

This makes the version go from ``X.Y.Z`` to ``X.Y.(Z+1)-dev``. The same can be done for Y and Z with
``bumpversion minor`` and ``bumpversion major``. To get rid of the ``-dev`` prefix (only do this just before releasing)
you can use ``bumpversion release``.

Note: you have to make sure you have a clean working directory before running this! That means no uncommitted files.

Releasing to PyPI
-----------------
PyPI is pronounced Py-Pee-Eye! After doing ``bumpversion release``, you should release to PyPI using the following:

.. code-block:: sh

    pip install wheel twine
    python setup.py -q sdist bdist_wheel
    twine upload --skip-existing dist/*

Remembering the bumpversion and release commands is a pain, so there's a magical command in ``tox.ini``
called finish that can be run like with ``tox -e finish``. It takes care of bumping the version to a release
version, making the distributions, pushing to PyPI, pushing to git, bumping the version with the next patch,
then pushing to git again.

.. |build| image:: https://travis-ci.com/cthoyt-teaches-reproducibility/iter-together-FINISHED.svg?branch=master
    :target: https://travis-ci.com/cthoyt-teaches-reproducibility/iter-together-FINISHED
    :alt: Build Status

.. |coverage| image:: https://codecov.io/gh/cthoyt-teaches-reproducibility/iter-together-FINISHED/coverage.svg?branch=master
    :target: https://codecov.io/gh/cthoyt-teaches-reproducibility/iter-together-FINISHED/branch/,aster
    :alt: Coverage Status

.. |documentation| image:: https://readthedocs.org/projects/cthoyt-teaches-reproducibility-iter-together-finished/badge/?version=latest
    :target: https://cthoyt-teaches-reproducibility-iter-together-finished.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |climate| image:: https://codeclimate.com/github/cthoyt-teaches-reproducibility/iter-together-FINISHED/badges/gpa.svg
    :target: https://codeclimate.com/github/cthoyt-teaches-reproducibility/iter-together-FINISHED
    :alt: Code Climate

.. |zenodo| image:: https://zenodo.org/badge/68376693.svg
    :target: https://zenodo.org/badge/latestdoi/68376693
