import os
import io
import sys
import unittest
from src.here_debugger.debug import here_debug

class TestHereDebugger(unittest.TestCase):
    file_name = os.path.basename(__file__)

    def test_here_debugger(self):
        # Capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Define test variables
        x = 10
        y = 'test'
        z = [1, 2, 3]

        # Call the function with the test variables
        here_debug(x, y, z)

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify print output
        expected_output = f"File: {self.file_name}: Line-21: x = 10 | y = test | z = [1, 2, 3] | "
        self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())

    def test_here_debugger_multiline(self):
        # Capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Define test variables
        x = 10
        y = "test"
        z = [1, 2, 3]

        # Call the function with the test variables, 2 times
        here_debug(x,y)
        here_debug(z)


        # Restore stdout
        sys.stdout = sys.__stdout__
        # Verify print output
        expected_output = f"File: {self.file_name}: Line-41: x = 10 | y = test | \nFile: {self.file_name}: Line-42: z = [1, 2, 3] |"
        self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())



    def test_here_debugger_with_custom_search_text(self):
        # Capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Define test variables
        x = 10

        # Call the function with a custom argument
        here_debug(x, custom_search_text="DEBUG")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify print output
        expected_output = f"DEBUG: File: {self.file_name}: Line-62: x = 10 | "
        self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())

    def test_here_debugger_with_include_types(self):
        # Capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Define test variables
        x = 10
        y = 'test'

        # Call the function with include_types=True
        here_debug(x, y, include_types=True)

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify print output
        expected_output = f"File: {self.file_name}: Line-81: x = 10, type = <class 'int'> | y = test, type = <class 'str'> | "
        self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())

    def test_here_debugger_with_no_input(self):
        # Capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function with no input
        here_debug()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify print output
        expected_output = ""
        self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())

    def test_here_debugger_with_constant_and_assignment(self):
        # Capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function with no assignment and a assignment
        a = 2
        here_debug("Here", a)

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify print output
        expected_output = f"File: {self.file_name}: Line-112: Here | a = 2 |"
        self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())

    def test_here_debugger_with_constant_and_assignment_with_include_types(self):
        # Capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function with no assignment and a assignment with include types
        a = 2
        here_debug("Here", a, include_types=True)

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify print output
        expected_output = f"File: {self.file_name}: Line-128: Here, type = <class 'str'> | a = 2, type = <class 'int'> |"
        self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())



