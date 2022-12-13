from tests.embark_test_classes import VisualEmbarkStageTest
from sessions.embark_user import test_user_02
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# TODO for improving this test: See if we can actually get the src attribute of the icons. Right now it's just 
# checking whether a user is kicked out after getting 6 questions wrong in a row.

class TestVocabSpacedReviewAlgorithm(VisualEmbarkStageTest):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName)
        self.word_pairs = {"church":"iglesia", "companion (male)":"compañero", "companion (female)":"compañera", "city":"ciudad", "Elder":"Élder (misionero)", "day":"día"}
        self.word_pairs_reverse = {v: k for k, v in self.word_pairs.items()}
        self.word_pairs_reverse["la iglesia"] = self.word_pairs_reverse["iglesia"]
        self.word_pairs_reverse["la ciudad"] = self.word_pairs_reverse["ciudad"]
        self.word_pairs_reverse["la compañera"] = self.word_pairs_reverse["compañera"]
        self.word_pairs_reverse["el compañero"] = self.word_pairs_reverse["compañero"]
        self.word_pairs_reverse["el día"] = self.word_pairs_reverse["día"]
        self.word_pairs_mod = {v: k for k, v in self.word_pairs_reverse.items()}

    def test_vocab_spaced_review_algorithm(self):
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
        self.click(e.vocab_concept_list_discovered_1)

        self.click(e.task_page_back_button)
        self.click(e.back_button)
        self.wait_for_element_to_be_clickable(e.spaced_review_start_button)
        self.click(e.spaced_review_start_button)
        self.validate_element_text(e.spaced_review_quadrants_prompt, "la iglesia")

        self.answerCorrect("iglesia")

        self.click(e.spaced_review_continue_button)

        self.wait_for_text_in_element(e.spaced_review_continue_button, "Done")
        self.click(e.spaced_review_continue_button)

        self.wait_for_element_to_be_clickable(e.move_up_one_day_button)
        self.click(e.move_up_one_day_button)
        self.reload()
        self.click(e.spaced_review_start_button)
        self.find(e.spaced_review_soundbite)
        self.click(e.spaced_review_soundbite_answer)
        self.click(e.spaced_review_soundbite_check_button)
        checkClass = self.get_element(e.spaced_review_soundbite_answer).get_attribute("class")
        if "inactive-incorrect-card" in checkClass:
            self.click(e.spaced_review_soundbite_mine_works_too_button)
        self.click(e.spaced_review_continue_button)
        self.click(e.spaced_review_continue_button)

        self.wait_for_element_to_be_clickable(e.move_up_one_day_button)
        self.click(e.move_up_one_day_button)
        self.reload()
        self.click(e.spaced_review_start_button)
        self.validate_element_text(e.spaced_review_quadrants_prompt, "church")
        # self.click(e.spaced_review_quadrants_answer1)
        self.answerCorrect("church", False)
        checkClass = self.get_element(e.spaced_review_quadrants_answer1).get_attribute("class")
        if "inactive-incorrect-card" in checkClass:
            self.click(e.spaced_review_mine_works_too_button)
        self.click(e.spaced_review_continue_button)
                
        # Strange thing here - before pressing Move Up One Day again, the typing activity shows up. Not sure why.

        action = ActionChains(self.driver)
        textarea = self.get_element(e.spaced_review_type_or_say_input)
        ActionChains(self.driver).move_to_element(textarea).send_keys("la iglesia").perform()
        self.wait_for_element_to_be_clickable(e.spaced_review_type_or_say_check)
        self.click(e.spaced_review_type_or_say_check)
        self.wait_for_element_to_be_clickable(e.spaced_review_typing_continue_button)
        self.click(e.spaced_review_typing_continue_button)
        self.click(e.spaced_review_continue_button)

        self.wait_for_element_to_be_clickable(e.move_up_one_day_button)
        for i in range(7):
            self.click(e.move_up_one_day_button)
        self.reload()
        self.click(e.spaced_review_start_button)
        
        textarea = self.get_element(e.spaced_review_type_or_say_input)
        ActionChains(self.driver).move_to_element(textarea).send_keys("la iglesia").perform()
        self.click(e.spaced_review_type_or_say_check)
        self.wait_for_element_to_be_clickable(e.spaced_review_typing_continue_button)
        self.click(e.spaced_review_typing_continue_button)
        self.click(e.spaced_review_continue_button)

        self.wait_for_element_to_be_clickable(e.move_up_one_day_button)
        for i in range(30):
            self.click(e.move_up_one_day_button)
        self.reload()
        self.click(e.spaced_review_start_button)
        
        textarea = self.get_element(e.spaced_review_type_or_say_input)
        ActionChains(self.driver).move_to_element(textarea).send_keys("la iglesia").perform()
        self.click(e.spaced_review_type_or_say_check)
        self.wait_for_element_to_be_clickable(e.spaced_review_typing_continue_button)
        self.click(e.spaced_review_typing_continue_button)
        self.click(e.spaced_review_continue_button)
        
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

    def answerCorrect(self, prompt, rev=True):
        e = self.elements
        self.answer1 = self.get_element(e.spaced_review_quadrants_answer1).text
        self.answer2 = self.get_element(e.spaced_review_quadrants_answer2).text
        self.answer3 = self.get_element(e.spaced_review_quadrants_answer3).text
        self.answer4 = self.get_element(e.spaced_review_quadrants_answer4).text
        if rev:
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
        else:
            if self.word_pairs_mod[prompt] == self.answer1:
                self.click(e.spaced_review_quadrants_answer1)
            elif self.word_pairs_mod[prompt] == self.answer2:
                self.click(e.spaced_review_quadrants_answer2)
            elif self.word_pairs_mod[prompt] == self.answer3:
                self.click(e.spaced_review_quadrants_answer3)
            elif self.word_pairs_mod[prompt] == self.answer4:
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