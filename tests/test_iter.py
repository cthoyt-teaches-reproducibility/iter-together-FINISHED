# -*- coding: utf-8 -*-

"""Tests for ``iter-together``."""

import unittest

from click.testing import CliRunner

from iter_together import cli, iter_together
from tests.constants import F1_PATH, F2_PATH


class TestIter(unittest.TestCase):
    """Test iterating files together."""

    def test_iter_together(self):
        """Test ``iter_together``."""
        expected = [
            ('a', 'a_1', 'a_2'),
            ('b', 'b_1', 'b_2'),
            ('c', 'c_1', 'c_2'),
            ('d', 'd_1', 'd_2'),
        ]
        actual = list(iter_together(F1_PATH, F2_PATH, sep=','))
        self.assertEqual(expected, actual)

    def test_cli(self):
        """Test the ``iter_together`` command line interface."""
        runner = CliRunner()
        args = [F1_PATH, F2_PATH]
        result = runner.invoke(cli.main, args)
        self.assertEqual(0, result.exit_code)
        expected_output = 'a,a_1,a_2\nb,b_1,b_2\nc,c_1,c_2\nd,d_1,d_2\n'
        self.assertEqual(expected_output, result.output)
