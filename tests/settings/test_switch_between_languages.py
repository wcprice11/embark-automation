from tests.embark_test_classes import EmbarkStageTest

class TestSwitchBetweenLanguages(EmbarkStageTest):
    def test_switch_between_languages(self):
        e = self.elements
        self.login("spanish")
        self.click(e.whats_new_card_close_button)
        self.click(e.settings_button)
        self.click(e.languages_button)
        self.click(e.language_manage_page_add_language_button)
        self.click(e.i_want_to_learn)
        self.click(e.learn_japanese)
        self.click(e.language_submit)
        self.wait_for_text_in_element(e.home_button, "Home")
        self.click(e.settings_button)
        check = self.get_element(e.loaded_language_subtext)
        self.validate_text(check.text, "Japanese (from English)")