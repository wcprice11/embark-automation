import unittest
import os.path

from HTMLTestRunner.runner import HTMLTestRunner
from tests.discover.record_audio import TestRecordAudio
from tests.discover.test_alphabet import TestStageDiscoverAlphabet
from tests.discover.test_discover import TestStageDiscoverVocab
from tests.settings.test_progress_updates_by_language import TestProgressUpdatesByLanguage
from tests.settings.test_sign_into_different_account import TestSignIntoDifferentAccount
from tests.settings.test_sound import TestSound
from tests.settings.test_switch_between_languages import TestSwitchBetweenLanguages


def run_single_class(testClass):
    test = unittest.TestLoader().loadTestsFromTestCase(testClass)

    if os.path.exists("report/additional-stylesheet.css"):
        with open("report/additional-stylesheet.css") as stylesheet:
            style = stylesheet.read()
    else:
        style = ""
    runner = HTMLTestRunner(log=True, verbosity=1, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport", tested_by="Christian Price",
                            add_traceback=True, style=style)

    runner.run(test)

if __name__ == "__main__":
    run_single_class(TestRecordAudio)