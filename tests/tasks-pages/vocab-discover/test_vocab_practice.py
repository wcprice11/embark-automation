from tests.embark_test_classes import EmbarkRCTest
from time import sleep
import random
from sessions.embark_user import test_user_02
from selenium.webdriver.common.action_chains import ActionChains

'''
Currently, this test:
1. Navigates to Meet Someone > Vocab > Practice
2. Does the Multiple Choice practice
3. Randomly chooses which questions to get right and wrong, and which path to take to deal with it

Future improvements:
1. Make tests for the other practice options. The typing one is mostly here, but it has issues so
we can leave it for later.
'''

class TestVocabPractice(EmbarkRCTest):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName)
        self.word_pairs = {"church":"iglesia",
         "companion (male)":"compañero", 
         "companion (female)":"compañera", 
         "city":"ciudad", 
         "Elder":"Élder (misionero)", 
         "day":"día",
         "family": "familia",
         "good": "bueno",
         "Good afternoon": "buenas tardes",
         "Good evening": "buenas noches",
         "Good morning": "buenos días",
         "home": "hogar",
         "Jesus Christ": "Jesucristo",
         "message": "mensaje",
         "missionary (male)": "misionero",
         "missionary (female)": "misionera",
         "name": "nombre",
         "school": "escuela",
         "to be (characteristic)": "ser",
         "to be (state)": "estar",
         "to bless": "bendecir",
         "to come": "venir",
         "to go": "ir",
         "to grow": "crecer",
         "to have": "tener",
         "to help": "ayudar",
         "to know (familiarity)": "conocer",
         "to live": "vivir",
         "to serve": "servir",
         "today": "hoy",
         "town": "pueblo",
         }
        self.word_pairs_reverse = {v: k for k, v in self.word_pairs.items()}
        self.word_pairs.update(self.word_pairs_reverse)

        pairs_with_articles = {"la iglesia": self.word_pairs_reverse["iglesia"],
                                "la ciudad": self.word_pairs_reverse["ciudad"],
                                "la compañera": self.word_pairs_reverse["compañera"],
                                "el compañero": self.word_pairs_reverse["compañero"],
                                "el día": self.word_pairs_reverse["día"]}
        pairs_with_articles_reverse = {v: k for k, v in pairs_with_articles.items()}
        self.word_pairs.update(pairs_with_articles)
        self.word_pairs.update(pairs_with_articles_reverse)

    def test_vocab_practice(self):
        e = self.elements
        self.load_user(test_user_02)
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
        self.wait_for_element_to_be_clickable(e.lesson_practice_button)
        self.click(e.lesson_practice_button)
        self.wait_for_element_to_be_clickable(e.lesson_practice_multiple_choice)
        self.click(e.lesson_practice_multiple_choice)
        self.click(e.start_button)

        done = False
        while not done:
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
                    self.click(e.lesson_practice_mine_works_too_button)
                elif mineWorksToo == 1:
                    self.click(e.lesson_practice_got_it_button)
                elif mineWorksToo == 2:
                    self.answerCorrect(prompt)
            completionNumbers = self.get_element(e.lesson_practice_header_progress_numbers).text
            slashpos = completionNumbers.index('/')
            completed = completionNumbers[0:slashpos]
            total = completionNumbers[slashpos+1:]
            if completed == total:
                done = True
            self.click(e.spaced_review_continue_button)
            

        feedback_text = self.get_element(e.lesson_practice_activity_feedback).text
        if feedback_text == "Congratulations!":
            self.click(e.lesson_practice_activity_continue)
        else:
            self.click(e.lesson_practice_close_button)
        
        # The code below had issues with returning to an input to put the correct answer, which is odd. 
        # We'll try and get it working later.

        # self.wait_for_element_to_be_clickable(e.lesson_practice_type_or_say)
        # self.click(e.lesson_practice_type_or_say)
        # self.click(e.start_button)
        # done = False
        # while not done:
        #     prompt = self.get_element(e.lesson_practice_type_or_say_prompt).text
        #     answerCorrect = random.randint(0, 1)
        #     mineWorksToo = random.randint(0, 1)
        #     sleep(1)
        #     if answerCorrect == 1:
        #         action = ActionChains(self.driver)
        #         textarea = self.get_element(e.lesson_practice_type_or_say_input)
        #         answer = self.word_pairs[prompt]
        #         move = ActionChains(self.driver).move_to_element(textarea)
        #         move.send_keys(answer).perform()
        #         self.click(e.lesson_practice_type_or_say_check)
        #     else:
        #         action = ActionChains(self.driver)
        #         textarea = self.get_element(e.lesson_practice_type_or_say_input)
        #         ActionChains(self.driver).move_to_element(textarea).send_keys("Nonsense").perform()
        #         self.click(e.lesson_practice_type_or_say_check)
        #         if mineWorksToo == 0:
        #             self.click(e.lesson_practice_type_or_say_mine_works_too)
        #         elif mineWorksToo == 1:
        #             self.click(e.lesson_practice_type_or_say_try_again)
        #             action = ActionChains(self.driver)
        #             textarea = self.get_element(e.lesson_practice_type_or_say_input)
        #             # ActionChains(self.driver).move_to_element(textarea).send_keys(self.word_pairs[prompt]).perform()
        #             answer = self.word_pairs[prompt]
        #             move = ActionChains(self.driver).move_to_element(textarea)
        #             self.click(e.lesson_practice_type_or_say_input_clear_button)
        #             move.send_keys(answer).perform()
        #             self.click(e.lesson_practice_type_or_say_check)
        #     self.click(e.lesson_practice_type_or_say_continue)
        #     completionNumbers = self.get_element(e.lesson_practice_header_progress_numbers).text
        #     slashpos = completionNumbers.index('/')
        #     completed = completionNumbers[0:slashpos]
        #     total = completionNumbers[slashpos+1:]
        #     if completed == total:
        #         done = True
        # self.click(e.lesson_practice_activity_continue)

    def answerCorrect(self, prompt):
        e = self.elements
        if self.word_pairs[prompt] == self.answer1:
            self.click(e.spaced_review_quadrants_answer1)
        elif self.word_pairs[prompt] == self.answer2:
            self.click(e.spaced_review_quadrants_answer2)
        elif self.word_pairs[prompt] == self.answer3:
            self.click(e.spaced_review_quadrants_answer3)
        elif self.word_pairs[prompt] == self.answer4:
            self.click(e.spaced_review_quadrants_answer4)
        else:
            self.failureException("Didn't find correct answer")

    def answerInorrect(self, prompt):
        e = self.elements
        if self.word_pairs[prompt] == self.answer1:
            self.click(e.spaced_review_quadrants_answer2)
        elif self.word_pairs[prompt] == self.answer2:
            self.click(e.spaced_review_quadrants_answer3)
        elif self.word_pairs[prompt] == self.answer3:
            self.click(e.spaced_review_quadrants_answer4)
        elif self.word_pairs[prompt] == self.answer4:
            self.click(e.spaced_review_quadrants_answer1)
