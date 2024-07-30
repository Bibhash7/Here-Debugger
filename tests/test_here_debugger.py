from src.here_debugger.debug import here_debugger
import unittest
import io
import sys
import inspect
from unittest.mock import patch


class TestHereDebugger(unittest.TestCase):

    def test_here_debugger(self):
        # Capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Define test variables
        x = 10
        y = 'test'
        z = [1, 2, 3]

        # Call the function with the test variables
        here_debugger(x, y, z)

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify print output
        expected_output = f"Line-{inspect.currentframe().f_lineno - 6}: x = 10, | y = test, | z = [1, 2, 3], | "
        self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())

    def test_here_debugger_with_custom_arguments(self):
        # Capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Define test variables
        x = 10

        # Call the function with a custom argument
        here_debugger(x, custom_arguments="DEBUG")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify print output
        expected_output = f"DEBUG:Line-{inspect.currentframe().f_lineno - 6}: x = 10, | "
        self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())

    def test_here_debugger_with_include_types(self):
        # Capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Define test variables
        x = 10
        y = 'test'

        # Call the function with include_types=True
        here_debugger(x, y, include_types=True)

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify print output
        expected_output = f"Line-{inspect.currentframe().f_lineno - 6}: x = 10, type=<class 'int'> | y = test, type=<class 'str'> | "
        self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())