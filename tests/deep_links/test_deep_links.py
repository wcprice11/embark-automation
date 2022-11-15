
from tests.embark_tests import EmbarkStageTest

class TestDeepLinks(EmbarkStageTest):
    def test_link_to_pray_often(self):
        self.login("spanish")
        self.wait_for_text_in_element(self.elements.whats_new_card_close_button, "Close")
        self.click(self.elements.whats_new_card_close_button)
        self.validate_element_text(self.elements.resources_button, "Resources")
        self.wait_for_element_to_be_clickable(self.elements.resources_button)
        self.click(self.elements.resources_button)
        self.click(self.elements.tip_pop_up_close)
        self.click(self.elements.spanish_resources_vocab)
        self.click(self.elements.resources_pray_often)
        elem = self.get_element(self.elements.pdf_header_title)
        self.validate_text(elem.text, "Pray Often")
        self.validate_url_contains("mediaItem/404778b5-1009-4d0c-ac2b-68307b2dd12d")
    
    def test_link_to_articles_lesson(self):
        self.login("spanish")
        self.wait_for_text_in_element(self.elements.whats_new_card_close_button, "Close")
        self.click(self.elements.whats_new_card_close_button)
        self.wait_for_element_to_be_clickable(self.elements.resources_button)
        self.click(self.elements.resources_button)
        self.click(self.elements.tip_pop_up_close)
        self.click(self.elements.spanish_resources_grammar)
        self.click(self.elements.spanish_grammar_articles)
        elem = self.get_element(self.elements.grammar_lesson_header)
        self.validate_text(elem.text,  "Grammar - Articles")
