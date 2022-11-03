from tests.embark_test_classes import EmbarkProdTest
from list_of_languages import languages, core_languages
from random import randint

# This will fail if any SEVERE console errors are found after the initial authentication.
class TestCatchConsoleErrors(EmbarkProdTest):
    def test_sample_all_languages(self):
        e = self.elements
        langs = []
        langs += languages[randint(0, len(languages)-1)]
        langs += languages[randint(0, len(languages)-1)]
        langs += languages[randint(0, len(languages)-1)]
        langs += languages[randint(0, len(languages)-1)]
        langs += languages[randint(0, len(languages)-1)]
        # login with random sample languages
        for lang in langs:
            with self.subTest(lang=lang):
                self.login()
                logs = self.driver.get_log('browser')
                self.i_want_to_learn(lang)
                for log in self.driver.get_log('browser'):
                    if(log["level"] == "SEVERE" and log not in logs):
                        self.fail(f"failed on {lang} with error:" + log["message"])
                self.wait_for_text_in_element(e.whats_new_card_close_button, "Close")
                self.click(e.whats_new_card_close_button)
                for log in self.driver.get_log('browser'):
                    if(log["level"] == "SEVERE" and log not in logs):
                        self.fail(f"failed on {lang} with error:" + log["message"])
                self.load_driver(self.driver)

    def test_core_languages(self):
        e = self.elements
        for lang in core_languages:
            with self.subTest(lang=lang):
                self.login()
                logs = self.driver.get_log('browser')
                self.i_want_to_learn(lang)
                for log in self.driver.get_log('browser'):
                    if(log["level"] == "SEVERE" and log not in logs):
                        self.fail(f"failed on {lang} with error:" + log["message"])
                self.wait_for_text_in_element(e.whats_new_card_close_button, "Close")
                self.click(e.whats_new_card_close_button)
                for log in self.driver.get_log('browser'):
                    if(log["level"] == "SEVERE" and log not in logs):
                        self.fail(f"failed on {lang} with error:" + log["message"])
                self.load_driver(self.driver)
