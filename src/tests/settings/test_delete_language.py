from tests.embark_tests import VisualEmbarkStageTest

class TestDeleteLanguage(VisualEmbarkStageTest):
    def test_delete_language(self):
        e = self.elements
        self.login("spanish")
        self.click(e.whats_new_card_close_button)
        self.click(e.settings_button)
        self.click(e.languages_button)
        language_name = self.get_element(e.language_select_page_language_name)
        print(language_name)
        self.click(e.language_select_page_delete_button)