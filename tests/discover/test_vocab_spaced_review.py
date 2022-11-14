from tests.embark_tests import VisualEmbarkStageTest
from selenium.webdriver.common.keys import Keys
from time import sleep
class TestVocabSpacedReview(VisualEmbarkStageTest):
    def test_vocab_spaced_review(self):
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
        self.click(e.lesson_card)
        self.wait_for_element_to_be_clickable(e.lesson_discover_button)
        self.click(e.lesson_discover_button)
        self.click(e.start_button)
        self.click(e.vocab_discover_right_arrow)
        self.click(e.vocab_discover_right_arrow)
        self.click(e.vocab_discover_right_arrow)
        self.click(e.vocab_discover_right_arrow)
        self.click(e.vocab_discover_right_arrow)
        self.click(e.vocab_discover_right_arrow)
        self.click(e.vocab_discover_take_quiz_button)

        word_pairs = {"church":"iglesia", "companion (male)":"compañero", "companion (female)":"compañera", "city":"ciudad", "Elder":"Élder (misionero)", "day":"día"}
        native_selectors = [e.vocab_discover_quiz_native_1, e.vocab_discover_quiz_native_2, e.vocab_discover_quiz_native_3, e.vocab_discover_quiz_native_4, e.vocab_discover_quiz_native_5, e.vocab_discover_quiz_native_6]
        target_selectors = [e.vocab_discover_quiz_target_1, e.vocab_discover_quiz_target_2, e.vocab_discover_quiz_target_3, e.vocab_discover_quiz_target_4, e.vocab_discover_quiz_target_5, e.vocab_discover_quiz_target_6]
        for i in range(6):
            for j in range(6):
                # self.get_element(e.vocab_discover_quiz_native_1)
                if word_pairs[self.get_element(native_selectors[i]).text] == self.get_element(target_selectors[j]).text:
                    self.click(native_selectors[i])
                    self.click(target_selectors[j])
        sleep(1)
        self.validate_element_text(e.vocab_discover_right_arrow, "Continue")