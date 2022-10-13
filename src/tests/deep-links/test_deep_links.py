
from tests.embark_tests import EmbarkStageTest

class TestDeepLinks(EmbarkStageTest):
    def test_link_to_pray_often(self):
        self.login("spanish")
        self.click(self.elements.whats_new_card_close_button)
        self.click(self.elements.resources_button)
        self.click(self.elements.spanish_resources_vocab)
        self.click(self.elements.resources_pray_often)
        self.validate_url_contains("mediaItem/404778b5-1009-4d0c-ac2b-68307b2dd12d")
        elem = self.find(self.elements.pdf_header_title)
        self.validate_text(elem.text, "Pray Often ")
    
    def test_link_to_articles_lesson(self):
        self.login("spanish")
        self.click(self.elements.whats_new_card_close_button)
        self.click(self.elements.resources_button)
        self.click(self.elements.spanish_resources_grammar)
        self.click(self.elements.spanish_grammar_articles)
        elem = self.find(self.elements.grammar_lesson_header)
        self.validate_text(elem.text,  "grammar - Articles ")
