from tests.embark_tests import VisualEmbarkStageTest
from sessions.embark_user import test_user_02

class TestSignIntoDifferentAccount(VisualEmbarkStageTest):
    def test_sign_into_different_account(self):

        # TODO: This file opens and closes the browser window because for some reason it doesn't actually fully logout on logout. 
        # We should figure out a way to do this without closing the browser window.

        e = self.elements
        self.login("spanish")
        self.click(e.whats_new_card_close_button)
        value1 = self.get_element(e.alphabet_progress_bar).get_attribute("value")
        self.click(e.settings_button)
        self.click(e.log_out_button)
        self.load_driver(self.driver)
        self.load_user(test_user_02)
        self.login("spanish")
        self.click(e.whats_new_card_close_button)
        value2 = self.get_element(e.alphabet_progress_bar).get_attribute("value")
        self.validate_text_absent(value1, value2)