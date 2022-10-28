from tests.embark_tests import VisualEmbarkStageTest
from sessions.embark_user import test_user_02

class TestSignIntoDifferentAccount(VisualEmbarkStageTest):
    def test_sign_into_different_account(self):
        e = self.elements
        self.login("spanish")
        self.click(e.whats_new_card_close_button)
        value1 = self.get_element(e.alphabet_progress_bar).get_attribute("value")
        self.click(e.settings_button)
        self.click(e.log_out_button)
        self.load_user(test_user_02)
        # self.get(self.urls.LOGIN)
        self.login("spanish")
        self.click(e.whats_new_card_close_button)
        value2 = self.get_element(e.alphabet_progress_bar).get_attribute("value")
        self.validate_text()