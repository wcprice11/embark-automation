
from tests.embark_test_classes import EmbarkProdTest

class TestProdLoadCoreLanguage(EmbarkProdTest):
    def test_settings_menu_says_core_language(self):
        self.login("Korean")
        self.wait_for_element_to_be_clickable(self.elements.whats_new_card_close_button)
        self.click(self.elements.whats_new_card_close_button)
        self.click(self.elements.settings_button)
        elem = self.get_element(self.elements.loaded_language_subtext)
        self.validate_text(elem.text, "Korean (from English)")
    
    def test_lessons_load_core_languages(self):
        self.login("Korean")
        self.wait_for_element_to_be_clickable(self.elements.whats_new_card_close_button)
        self.click(self.elements.whats_new_card_close_button)
        self.click(self.elements.basic_tab)
        self.find(self.elements.tip_pop_up_close)
        self.click(self.elements.tip_pop_up_close)
        self.click(self.elements.basic_alphabet_card)
        elem = self.get_element(self.elements.first_card_in_alphabet)
        self.validate_text(elem.text, "ㄱ")
