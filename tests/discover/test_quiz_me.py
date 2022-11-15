from tests.embark_tests import EmbarkStageTest
from time import sleep
class TestQuizMe(EmbarkStageTest):
    def test_quiz_me(self):
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

        # Take first Spanish vocab quiz. This is super slow
        word_pairs = {"church":"iglesia", "companion (male)":"compañero", "companion (female)":"compañera", "city":"ciudad", "Elder":"Élder (misionero)", "day":"día"}
        native_selectors = [e.vocab_discover_quiz_native_1, e.vocab_discover_quiz_native_2, e.vocab_discover_quiz_native_3, e.vocab_discover_quiz_native_4, e.vocab_discover_quiz_native_5, e.vocab_discover_quiz_native_6]
        target_selectors = [e.vocab_discover_quiz_target_1, e.vocab_discover_quiz_target_2, e.vocab_discover_quiz_target_3, e.vocab_discover_quiz_target_4, e.vocab_discover_quiz_target_5, e.vocab_discover_quiz_target_6]
        skip_set = set()
        for i in range(6):
            for j in range(6):
                if j not in skip_set:
                    if word_pairs[self.get_element(native_selectors[i]).text] == self.get_element(target_selectors[j]).text:
                        self.click(native_selectors[i])
                        self.click(target_selectors[j])
                        skip_set.add(j)
        self.wait_for_text_in_element(e.vocab_discover_right_arrow, "Continue")
        self.click(e.vocab_discover_right_arrow)
        self.wait_for_text_in_element(e.lesson_discover_flashcard_text, "la familia")
        self.find(e.lesson_discover_toolbar)
        self.click(e.close_button)

        for i in range(2):
            self.click(e.vocab_concept_list_discovered_1)
            self.click(e.vocab_concept_list_discovered_2)
            self.click(e.vocab_concept_list_discovered_3)
            self.click(e.vocab_concept_list_discovered_4)
            self.click(e.vocab_concept_list_discovered_5)
            self.click(e.vocab_concept_list_discovered_6)