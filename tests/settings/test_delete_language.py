from tests.embark_test_classes import EmbarkRCTest

class TestDeleteLanguage(EmbarkRCTest):
    def test_delete_language(self):
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
        self.click(e.languages_button)
        language_name = self.get_element(e.language_manage_page_language_name).text
        self.click(e.language_manage_page_delete_button)
        self.click(e.language_manage_page_confirm_delete_button)
        check = self.get_element(e.language_manage_page_language_name)   
        self.validate_text_absent(language_name, check.text)
        # We could put this in a while loop  and have it delete more languages, then check if it only has one language left
