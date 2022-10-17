# Running Tests

The full test suite can be run with the `embark_test_runner.py` script. 
Alternately, individual tests can be run from the command line via the `unittest` module.
To run a test, pass the test to unittest as follows `tests.[submodule].[test name]` For example:

Windows:
`python -m unittest tests.general.test_login`

MacOS
`python3 -m unittest tests.general.test_login`