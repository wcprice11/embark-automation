from tests.embark_tests import VisualEmbarkStageTest

class TestStageDiscoverAlphabet(VisualEmbarkStageTest):
    def test_alphabet_discover(self):
        e = self.elements
        self.login("spanish")
        self.click(e.whats_new_card_close_button)
        # Check if in recommended
        self.validate_element_text(e.recommended_alphabet_lesson_title, "Alphabet")
        self.click(e.recommended_alphabet_lesson)
        self.wait_for_text_in_element(e.page_title, "Alphabet")
        self.validate_element_text(e.lesson_section_title, "Essentials")
        self.validate_element_text(e.lesson_card, "Symbols and Sounds")
        self.click(e.back_button)
        self.wait_for_text_in_element(e.page_title, "Alphabet")
        self.click(e.basic_tab)
        self.wait_for_text_in_element(e.basic_alphabet_card, "Alphabet")
        self.click(e.basic_alphabet_card)
        self.wait_for_text_in_element(e.page_title, "Alphabet")
        self.validate_element_text(e.lesson_section_title, "Essentials")
        self.validate_element_text(e.lesson_card, "Symbols and Sounds")
        self.click(e.lesson_card)
        self.wait_for_text_in_element(e.page_title, "Alphabet")
        
        pass

