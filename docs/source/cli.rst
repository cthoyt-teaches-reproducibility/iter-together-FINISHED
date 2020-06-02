Command Line Interface
======================
.. note:: The command line wrapper might not work on Windows. Use :code:`python3 -m iter_together` if it has issues.

``iter-together`` automatically installs the command :code:`iter-together`. This command can be used to use
the :func:`iter_together.iter_together` function via the command line.

.. click:: iter_together.cli:main
   :prog: iter-together
   :show-nested:
