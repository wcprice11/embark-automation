from tests.embark_test_classes import VisualEmbarkRCTest
from selenium.webdriver.common.by import By

'''
Right now, this test:
1. navigates to the first vocab discover quiz in Spanish
2. It gets all of the quiestions right
3. Then navigates back to the main page and clears progress.


Future ideas: Get questions wrong and make sure behavior is correct
'''

class TestQuizMe(VisualEmbarkRCTest):
    def test_quiz_me(self):
        e = self.elements
        self.login("spanish")
        self.wait_for_text_in_element(e.whats_new_card_close_button, "Close")
        self.click(e.whats_new_card_close_button)
        self.find(e.recommended_meet_someone_lesson)
        self.validate_element_text(e.recommended_meet_someone_lesson, "Meet Someone\nBasic")
        self.click(e.recommended_meet_someone_lesson)
        self.wait_for_text_in_element(e.page_title, "Meet Someone")
        self.validate_element_text(e.lesson_section_title, "Essentials")
        self.validate_element_text(e.lesson_card, "Vocabulary")
        self.click(e.lesson_card)
        
        self.markWords("")

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

        # Take first Spanish vocab quiz. This is super slow, see if we can speed it up
        word_pairs = {"church":"iglesia", "companion (male)":"compañero", "companion (female)":"compañera", "city":"ciudad", "Elder":"Élder (misionero)", "day":"día"}
        base_native_selector_1 = "app-matching-quiz>div:nth-of-type("
        base_native_selector_2 = ")"
        base_native_descriptor_1 = "Native language item "
        base_native_descriptor_2 = " in quiz"
        base_target_selector_1 = "app-matching-quiz>div:nth-of-type("
        base_target_selector_2 = ")"
        base_target_descriptor_1 = "Target language item "
        base_target_descriptor_2 = " in quiz"
        skip_set = set()
        for i in range(6):
            for j in range(6):
                if j not in skip_set:
                    native_selector = (By.CSS_SELECTOR, base_native_selector_1 + str(i+1) + base_native_selector_2, base_native_descriptor_1 + str(i+1) + base_native_descriptor_2)
                    target_selector = (By.CSS_SELECTOR, base_target_selector_1 + str(j+7) + base_target_selector_2, base_target_descriptor_1 + str(j+7) + base_target_descriptor_2)
                    if word_pairs[self.get_element(native_selector).text] == self.get_element(target_selector).text:
                    # if word_pairs[self.get_element(native_selectors[i]).text] == self.get_element(target_selectors[j]).text:
                        # self.click(native_selectors[i])
                        # self.click(target_selectors[j])
                        self.click(native_selector)
                        self.click(target_selector)
                        skip_set.add(j)
        self.click(e.vocab_discover_right_arrow)
        self.wait_for_text_in_element(e.lesson_discover_flashcard_text, "bueno")
        self.click(e.close_button)

        self.markWords("")


    def markWords(self, target):
        if target == "mastered":
            target_name = "checkmark-done-circle"
        elif target == "discovered":
            target_name = "checkmark-circle-outline"
        else:
            target_name = "ellipse-outline"
        base_sel_1 = "app-task-study-list>ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item:nth-of-type("
        base_sel_2 = ")>ion-icon:nth-of-type(3)"
        base_label = "Discovered button in vocab list "
        for i in range(6):
            sel = (By.CSS_SELECTOR, base_sel_1 + str(i+2) + base_sel_2, base_label + str(i+1))
            name = self.get_element(sel).get_attribute("name")
            while name != target_name:
                self.click(sel)
                name = self.get_element(sel).get_attribute("name")