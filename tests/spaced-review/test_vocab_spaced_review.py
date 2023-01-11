from tests.embark_test_classes import EmbarkRCTest
from selenium.webdriver.common.by import By
import random
from sessions.embark_user import test_user_02

'''
This test currently:
1. Navigates to Meet Someone > Vocab and does the first quiz
2. Goes to Spaced Review from the task page and goes through the first day. 
3. It chooses randomly whether to get a question right or wrong, and handles the situation accordingly.

'''

class TestDiscoverToSpacedReview(EmbarkRCTest):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName)
        self.word_pairs = {"church":"iglesia", "companion (male)":"compañero", "companion (female)":"compañera", "city":"ciudad", "Elder":"Élder (misionero)", "day":"día"}
        self.word_pairs_reverse = {v: k for k, v in self.word_pairs.items()}
        self.word_pairs_reverse["la iglesia"] = self.word_pairs_reverse["iglesia"]
        self.word_pairs_reverse["la ciudad"] = self.word_pairs_reverse["ciudad"]
        self.word_pairs_reverse["la compañera"] = self.word_pairs_reverse["compañera"]
        self.word_pairs_reverse["el compañero"] = self.word_pairs_reverse["compañero"]
        self.word_pairs_reverse["el día"] = self.word_pairs_reverse["día"]

    def test_discover_to_spaced_review(self):
        e = self.elements
        self.load_user(test_user_02)
        self.login("spanish")
        self.wait_for_text_in_element(e.whats_new_card_close_button, "Close")
        self.click(e.whats_new_card_close_button)

        # Check if in recommended
        self.find(e.recommended_meet_someone_lesson)
        self.validate_element_text(e.recommended_meet_someone_lesson, "Meet Someone\nBasic")
        self.click(e.recommended_meet_someone_lesson)
        self.validate_element_text(e.lesson_card, "Vocabulary")
        self.click(e.lesson_card)
        self.wait_for_element_to_be_clickable(e.lesson_discover_button)

        self.clearProgress()       

        # Move to quiz
        self.click(e.lesson_discover_button)
        self.click(e.start_button)
        self.click(e.vocab_discover_right_arrow)
        self.click(e.vocab_discover_right_arrow)
        self.click(e.vocab_discover_right_arrow)
        self.click(e.vocab_discover_right_arrow)
        self.click(e.vocab_discover_right_arrow)
        self.click(e.vocab_discover_right_arrow)
        self.click(e.vocab_discover_take_quiz_button)

        # Take first Spanish vocab quiz. This is super slow, working on speeding it up
        base_native_selector_1 = "app-matching-quiz>div:nth-of-type("
        base_native_selector_2 = ")"
        base_native_descriptor_1 = "Native language item "
        base_native_descriptor_2 = " in quiz"
        base_target_selector_1 = "app-matching-quiz>div:nth-of-type("
        base_target_selector_2 = ")"
        base_target_descriptor_1 = "Target language item "
        base_target_descriptor_2 = " in quiz"
        skip_set = set()
        word_pairs = {"church":"iglesia", "companion (male)":"compañero", "companion (female)":"compañera", "city":"ciudad", "Elder":"Élder (misionero)", "day":"día"}
        for i in range(6):
            for j in range(6):
                if j not in skip_set:
                    native_selector = (By.CSS_SELECTOR, base_native_selector_1 + str(i+1) + base_native_selector_2, base_native_descriptor_1 + str(i+1) + base_native_descriptor_2)
                    target_selector = (By.CSS_SELECTOR, base_target_selector_1 + str(j+7) + base_target_selector_2, base_target_descriptor_1 + str(j+7) + base_target_descriptor_2)
                    if word_pairs[self.get_element(native_selector).text] == self.get_element(target_selector).text:
                        self.click(native_selector)
                        self.click(target_selector)
                        skip_set.add(j)
        self.click(e.vocab_discover_right_arrow)
        self.wait_for_text_in_element(e.lesson_discover_flashcard_text, "la familia")
        self.click(e.close_button)

        # Spaced review section
        self.wait_for_element_to_be_clickable(e.lesson_spaced_review_button)
        self.click(e.lesson_spaced_review_button)

        done = False
        while not done:
            buttonText = self.get_element(e.spaced_review_continue_button).text
            if buttonText == "Done":
                break
            prompt = self.get_element(e.spaced_review_quadrants_prompt).text
            self.answer1 = self.get_element(e.spaced_review_quadrants_answer1).text
            self.answer2 = self.get_element(e.spaced_review_quadrants_answer2).text
            self.answer3 = self.get_element(e.spaced_review_quadrants_answer3).text
            self.answer4 = self.get_element(e.spaced_review_quadrants_answer4).text
            answerCorrect = random.randint(0, 1)
            mineWorksToo = random.randint(0, 2)
            if answerCorrect == 1:
                self.answerCorrect(prompt)
            if answerCorrect == 0:
                self.answerInorrect(prompt)
                if mineWorksToo == 0:
                    self.click(e.spaced_review_mine_works_too_button)
                elif mineWorksToo == 1:
                    self.click(e.spaced_review_got_it_button)
                elif mineWorksToo == 2:
                    self.answerCorrect(prompt)
            buttonText = self.get_element(e.spaced_review_continue_button).text
            if buttonText == "Done":
                done = True
            elif buttonText == "Continue":
                self.click(e.spaced_review_continue_button)

        self.wait_for_text_in_element(e.spaced_review_continue_button, "Done")
        self.click(e.spaced_review_continue_button)

        self.clearProgress()

    def answerCorrect(self, prompt):
        e = self.elements
        if self.word_pairs_reverse[prompt] == self.answer1:
            self.click(e.spaced_review_quadrants_answer1)
        elif self.word_pairs_reverse[prompt] == self.answer2:
            self.click(e.spaced_review_quadrants_answer2)
        elif self.word_pairs_reverse[prompt] == self.answer3:
            self.click(e.spaced_review_quadrants_answer3)
        elif self.word_pairs_reverse[prompt] == self.answer4:
            self.click(e.spaced_review_quadrants_answer4)
        else:
            self.failureException("Didn't find correct answer")

    def answerInorrect(self, prompt):
        e = self.elements
        if self.word_pairs_reverse[prompt] == self.answer1:
            self.click(e.spaced_review_quadrants_answer2)
        elif self.word_pairs_reverse[prompt] == self.answer2:
            self.click(e.spaced_review_quadrants_answer3)
        elif self.word_pairs_reverse[prompt] == self.answer3:
            self.click(e.spaced_review_quadrants_answer4)
        elif self.word_pairs_reverse[prompt] == self.answer4:
            self.click(e.spaced_review_quadrants_answer1)

    def clearProgress(self):
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