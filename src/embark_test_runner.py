import unittest
import os.path

from HTMLTestRunner.runner import HTMLTestRunner
from tests.deep_links.test_deep_links import TestDeepLinks


def run_full_suite():
    l = unittest.TestLoader()
    suite = l.discover("./src/tests", "test*.py", ".")

    if os.path.exists("report/additional-stylesheet.css"):
        with open("report/additional-stylesheet.css") as stylesheet:
            style = stylesheet.read()

    runner = HTMLTestRunner(log=True, verbosity=1, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport", tested_by="Christian Price",
                            add_traceback=True, style=style)

    runner.run(suite)

def run_single_class(testClass):
    test = unittest.TestLoader().loadTestsFromTestCase(testClass)

    if os.path.exists("report/additional-stylesheet.css"):
        with open("report/additional-stylesheet.css") as stylesheet:
            style = stylesheet.read()
    runner = HTMLTestRunner(log=True, verbosity=1, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport", tested_by="Christian Price",
                            add_traceback=True, style=style)

    runner.run(test)

if __name__ == "__main__":
    # run_full_suite()
    run_single_class(TestDeepLinks)
