import unittest
import os.path

from HTMLTestRunner.runner import HTMLTestRunner
from tests.test_login import *
from tests.test_language_select_screen import *

tests = []
tests += unittest.TestLoader().loadTestsFromTestCase(TestProdLogin)
tests += unittest.TestLoader().loadTestsFromTestCase(TestStageLogin)
tests += unittest.TestLoader().loadTestsFromTestCase(TestRCLogin)
tests += unittest.TestLoader().loadTestsFromTestCase(TestDevLogin)
tests += unittest.TestLoader().loadTestsFromTestCase(TestProdLanguageSelectScreen)
tests += unittest.TestLoader().loadTestsFromTestCase(TestStageLanguageSelectScreen)
tests += unittest.TestLoader().loadTestsFromTestCase(TestRCLanguageSelectScreen)
tests += unittest.TestLoader().loadTestsFromTestCase(TestDevLanguageSelectScreen)


suite = unittest.TestSuite(tests)

if os.path.exists("report/additional-stylesheet.css"):
    with open("report/additional-stylesheet.css") as stylesheet:
        style = stylesheet.read()

runner = HTMLTestRunner(log=True, verbosity=1, output='report', title='Test report', report_name='report',
                        open_in_browser=True, description="HTMLTestReport", tested_by="Christian Price",
                        add_traceback=True, style=style)

runner.run(suite)