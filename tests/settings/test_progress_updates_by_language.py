from tests.embark_test_classes import EmbarkRCTest

class TestProgressUpdatesByLanguage(EmbarkRCTest):
    def test_progress_updates_by_languages(self):
        e = self.elements
        self.login("spanish")
        self.click(e.whats_new_card_close_button)
        value1 = self.get_element(e.alphabet_progress_bar).get_attribute("value")
        self.click(e.settings_button)
        self.click(e.languages_button)
        self.click(e.language_manage_page_add_language_button)
        self.click(e.i_want_to_learn)
        self.click(e.learn_polish)
        self.click(e.language_submit)
        self.wait_for_text_in_element(e.home_button, "Home")
        value2 = self.get_element(e.alphabet_progress_secondary_language).get_attribute("value")
        self.validate_text_absent(value1, value2)