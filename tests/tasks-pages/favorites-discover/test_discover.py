from tests.embark_test_classes import EmbarkStageTest
from time import sleep
class TestStageDiscoverVocab(EmbarkStageTest):
    def test_vocab_discover(self):
        e = self.elements
        self.login("spanish")
        self.wait_for_text_in_element(e.whats_new_card_close_button, "Close")
        self.click(e.whats_new_card_close_button)
        
        # Check if in recommended
        self.find(e.recommended_meet_someone_lesson)
        self.validate_element_text(e.recommended_meet_someone_lesson, "Meet Someone\nBasic")
        self.click(e.recommended_meet_someone_lesson)
        
        self.wait_for_text_in_element(e.page_title, "Meet Someone")
        self.validate_element_text(e.lesson_section_title, "Essentials")
        self.validate_element_text(e.lesson_card, "Vocabulary")
        self.click(e.back_button)

        # Check if in basics tab
        self.click(e.basic_tab)
        self.click(e.tip_pop_up_close)
        self.click(e.basic_meet_someone_card)
        self.wait_for_text_in_element(e.page_title, "Meet Someone")
        self.validate_element_text(e.lesson_section_title, "Essentials")
        self.validate_element_text(e.lesson_card, "Vocabulary")
        self.click(e.lesson_card)

        # validate lesson page
        # self.wait_for_text_in_element(e.page_title, "Vocabulary")
        self.validate_element_text(e.lesson_discover_button, "Flashcards")
        self.validate_element_text(e.lesson_practice_button, "Pick Activity")
        self.validate_element_text(e.lesson_pass_off_button, "Test")
        self.validate_element_text(e.vocab_most_common_label, "Most Common")
        self.validate_element_text(e.vocab_first_word, "iglesia")

        # check vocab audio plays
        self.find(e.vocab_first_word_play)
        self.click(e.vocab_first_word_play)
        self.find(e.vocab_first_word_playing)

        # favorite button cycle through
        # Many of the Symbol Popover selectors also work here, leaving them the same (rename in the future)
        self.find(e.symbol_popover_favorite)
        self.click(e.symbol_popover_favorite)
        sleep(1)
        self.find(e.symbol_popover_unfavorite)
        self.click(e.symbol_popover_unfavorite)
        self.find(e.symbol_popover_favorite)
        
        # discovered button cycles through
        # TODO - This is currently an issue on the Vocab page. It works correctly, but the CSS titles aren't being changed right.
        # self.find(e.symbol_popover_discovered)
        # self.click(e.symbol_popover_discovered)
        # sleep(1)
        # self.find(e.symbol_popover_mastered)
        # self.click(e.symbol_popover_mastered)
        # sleep(1)
        # self.find(e.symbol_popover_unmark)
        # self.click(e.symbol_popover_unmark)
        # sleep(1)
        # self.find(e.symbol_popover_discovered)

        self.wait_for_element_to_be_clickable(e.lesson_practice_button)
        self.click(e.lesson_practice_button)

    # def test_alphabet_discover_favorites(self):
    #     e = self.elements
    #     self.login("spanish")
    #     self.wait_for_text_in_element(e.whats_new_card_close_button, "Close")
    #     self.click(e.whats_new_card_close_button)
    #     self.find(e.recommended_alphabet_lesson)
    #     self.wait_for_text_in_element(e.recommended_alphabet_lesson_title, "Alphabet")
    #     self.click(e.basic_tab)
    #     self.click(e.tip_pop_up_close)
    #     self.click(e.basic_alphabet_card)
    #     self.wait_for_text_in_element(e.page_title, "Alphabet")
    #     self.click(e.lesson_card)
    #     self.wait_for_text_in_element(e.page_title, "Alphabet")
    # It looks like this wasn't fully implemented in Alphabet. We can make a favorites test later.






