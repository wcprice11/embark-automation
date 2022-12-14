from tests.embark_test_classes import VisualEmbarkRCTest
from selenium.webdriver.common.by import By
from sessions.embark_user import test_user_02

'''
This test:
1. Navigates to Meet Someone > Vocab. 
2. Marks the first 6 words as Discovered.
3. Navigates back to the main page and goes to Spaced Review.
4. Gets all the questions correct.
5. Checks that progress on the Spaced Review card is correct.

Ideas for future improvement:
1. We could try refreshing or logging out. It's doing all it needs to for now.
'''


class TestSpacedReviewProgressSaves(VisualEmbarkRCTest):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName)
        self.word_pairs = {"church":"iglesia", "companion (male)":"compañero", "companion (female)":"compañera", "city":"ciudad", "Elder":"Élder (misionero)", "day":"día"}
        self.word_pairs_reverse = {v: k for k, v in self.word_pairs.items()}
        self.word_pairs_reverse["la iglesia"] = self.word_pairs_reverse["iglesia"]
        self.word_pairs_reverse["la ciudad"] = self.word_pairs_reverse["ciudad"]
        self.word_pairs_reverse["la compañera"] = self.word_pairs_reverse["compañera"]
        self.word_pairs_reverse["el compañero"] = self.word_pairs_reverse["compañero"]
        self.word_pairs_reverse["el día"] = self.word_pairs_reverse["día"]

    def test_spaced_review_progress_saves(self):
        e = self.elements
        self.load_user(test_user_02)
        self.login("spanish")
        self.wait_for_text_in_element(e.whats_new_card_close_button, "Close")
        self.click(e.whats_new_card_close_button)
        self.click(e.recommended_meet_someone_lesson)
        self.validate_element_text(e.lesson_card, "Vocabulary")
        self.click(e.lesson_card)
        self.wait_for_element_to_be_clickable(e.lesson_discover_button)

        self.markWords("")
        self.markWords("discovered")

        self.click(e.task_page_back_button)
        self.click(e.back_button)
        self.validate_element_text(e.spaced_review_number_to_do, "0 / 6 Questions")
        self.click(e.spaced_review_start_button)

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
            self.answerCorrect(prompt)
            
            buttonText = self.get_element(e.spaced_review_continue_button).text
            if buttonText == "Done":
                done = True
            elif buttonText == "Continue":
                self.click(e.spaced_review_continue_button)

        self.wait_for_text_in_element(e.spaced_review_continue_button, "Done")
        self.click(e.spaced_review_continue_button)

        self.validate_element_text(e.spaced_review_number_to_do, "0 / 0 Questions")

        self.click(e.recommended_meet_someone_lesson)
        self.validate_element_text(e.lesson_card, "Vocabulary")
        self.click(e.lesson_card)
        self.wait_for_element_to_be_clickable(e.lesson_discover_button)

        self.markWords("")


    def markWords(self, target):
        e = self.elements
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