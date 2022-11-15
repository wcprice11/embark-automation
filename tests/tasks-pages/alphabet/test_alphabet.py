from tests.embark_test_classes import EmbarkStageTest
from selenium.webdriver.common.keys import Keys
from time import sleep
class TestStageDiscoverAlphabet(EmbarkStageTest):
    def test_alphabet_discover_symbol_view(self):
        e = self.elements
        self.login("spanish")
        self.wait_for_text_in_element(e.whats_new_card_close_button, "Close")
        self.click(e.whats_new_card_close_button)
        # Check if in recommended
        self.find(e.recommended_alphabet_lesson)
        self.validate_element_text(e.recommended_alphabet_lesson_title, "Alphabet")
        self.click(e.recommended_alphabet_lesson)
        self.wait_for_text_in_element(e.page_title, "Alphabet")
        self.validate_element_text(e.lesson_section_title, "Essentials")
        self.validate_element_text(e.lesson_card, "Symbols and Sounds")
        self.click(e.back_button)
        # Check if in basics tab
        self.wait_for_text_in_element(e.page_title, "Alphabet")
        self.click(e.basic_tab)
        self.click(e.tip_pop_up_close)
        self.click(e.basic_alphabet_card)
        self.wait_for_text_in_element(e.page_title, "Alphabet")
        self.validate_element_text(e.lesson_section_title, "Essentials")
        self.validate_element_text(e.lesson_card, "Symbols and Sounds")
        self.click(e.lesson_card)
        # validate lesson page
        self.wait_for_text_in_element(e.page_title, "Alphabet")
        self.validate_element_text(e.lesson_discover_button, "Flashcards")
        self.validate_element_text(e.lesson_practice_button, "Pick Activity")
        self.validate_element_text(e.lesson_pass_off_button, "Test")
        self.validate_element_text(e.alphabet_first_letter, "a")
        # check symbol popover
        self.click(e.alphabet_first_letter)
        self.validate_element_text(e.symbol_popover_symbols, "A\na")
        self.find(e.symbol_popover_play)
        self.click(e.symbol_popover_play)
        self.find(e.symbol_popover_playing)

        # examples play
        self.validate_element_text(e.symbol_popover_example, "padre")
        self.find(e.symbol_popover_example_play)
        self.click(e.symbol_popover_example_play)
        self.find(e.symbol_popover_example_playing)
        self.find(e.symbol_popover_example_play)

        # favorite button cycle through
        self.find(e.symbol_popover_favorite)
        self.click(e.symbol_popover_favorite)
        sleep(1)
        self.find(e.symbol_popover_unfavorite)
        self.click(e.symbol_popover_unfavorite)
        self.find(e.symbol_popover_favorite)
        
        # discovered button cycles through
        self.find(e.symbol_popover_discovered)
        self.click(e.symbol_popover_discovered)
        sleep(1)
        self.find(e.symbol_popover_mastered)
        self.click(e.symbol_popover_mastered)
        sleep(1)
        self.find(e.symbol_popover_unmark)
        self.click(e.symbol_popover_unmark)
        sleep(1)
        self.find(e.symbol_popover_discovered)

        # exit
        self.get_element(e.body).send_keys(Keys.ESCAPE)
        self.wait_for_element_to_be_clickable(e.lesson_practice_button)
        self.click(e.lesson_practice_button)

        # Don't have a method to test the audio directly. 
        # Right now this is doing a soft test on playing audio by watching for the visual class change.
        # No microphone controls that I know of.

    def test_alphabet_discover_favorites(self):
        e = self.elements
        self.login("spanish")
        self.wait_for_text_in_element(e.whats_new_card_close_button, "Close")
        self.click(e.whats_new_card_close_button)
        self.find(e.recommended_alphabet_lesson)
        self.wait_for_text_in_element(e.recommended_alphabet_lesson_title, "Alphabet")
        self.click(e.basic_tab)
        self.click(e.tip_pop_up_close)
        self.click(e.basic_alphabet_card)
        self.wait_for_text_in_element(e.page_title, "Alphabet")
        self.click(e.lesson_card)
        self.wait_for_text_in_element(e.page_title, "Alphabet")





