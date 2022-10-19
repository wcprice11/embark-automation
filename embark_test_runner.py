import unittest
import os.path
from HTMLTestRunner.runner import HTMLTestRunner


def run_full_suite():
    l = unittest.TestLoader()
    suite = l.discover("./tests", "test*.py", ".")

    if os.path.exists("report/additional-stylesheet.css"):
        with open("report/additional-stylesheet.css") as stylesheet:
            style = stylesheet.read()
    else:
        style = ""

    runner = HTMLTestRunner(log=True, verbosity=1, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport", tested_by="Christian Price",
                            add_traceback=True, style=style)

    runner.run(suite)

if __name__ == "__main__":
    run_full_suite()
