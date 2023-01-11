from tests.embark_test_classes import EmbarkRCTest

class TestTonesInMandarin(EmbarkRCTest):
    def test_tones_in_mandarin(self):
        e = self.elements
        self.login("mandarin")
        self.wait_for_text_in_element(e.whats_new_card_close_button, "Close")
        self.click(e.whats_new_card_close_button)
        self.click(e.home_button)
        self.validate_element_text(e.recommended_tones_lesson, "Tones")
        self.click(e.recommended_tones_lesson)
        self.wait_for_text_in_element(e.tones_main_header, "Tones")
        self.find(e.tones_main_header)
        self.validate_url(self.urls.TONES_LESSON)
        self.validate_element_text(e.page_title, "Tones")
        self.validate_url(self.urls.TONES_LESSON)
        self.validate_element_text(e.individual_tones_first, "ˉ\n1st")
        self.validate_element_text(e.individual_tones_second, "ˊ\n2nd")
        self.validate_element_text(e.individual_tones_third, "ˇ\n3rd")
        self.validate_element_text(e.individual_tones_fourth, "ˋ\n4th")
        self.validate_element_text(e.individual_tones_fifth, "5th")
        self.click(e.tones_selector)
        self.validate_element_text(e.tones_option_combinations, "Tone Combinations")
        self.click(e.tones_option_combinations)
        self.wait_for_text_in_element(e.tones_selector, "Tone Combinations")
        self.validate_element_text(e.combination_tones_first, "1st\nˉ ˉ\nˉ ˊ\nˉ ˇ\nˉ ˋ\nˉ  ")
        self.validate_element_text(e.combination_tones_second, "2nd\nˊ ˉ\nˊ ˊ\nˊ ˇ\nˊ ˋ\nˊ  ")
        self.validate_element_text(e.combination_tones_third, "3rd\nˇ ˉ\nˇ ˊ\nˇ ˇ\nˇ ˋ\nˇ  ")
        self.validate_element_text(e.combination_tones_fourth, "4th\nˋ ˉ\nˋ ˊ\nˋ ˇ\nˋ ˋ\nˋ  ")