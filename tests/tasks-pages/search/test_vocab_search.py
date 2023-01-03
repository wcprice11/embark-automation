from tests.embark_test_classes import VisualEmbarkRCTest
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
from sessions.embark_user import test_user_02

class TestVocabSearch(VisualEmbarkRCTest):

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

    def test_vocab_search(self):
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

        self.click(e.task_page_search_button)
        self.fill(e.task_page_search_input, "asdfasdf")
        self.validate_element_text(e.task_page_search_no_results, "No Results")
        self.validate_element_text(e.task_page_search_try_a_new_search, "Try a new search.")
        self.click(e.task_page_search_clear_button)
        self.fill(e.task_page_search_input, "mis")
        self.validate_element_text(e.task_page_search_result_1_target_text, "Élder (misionero)")
        self.validate_element_text(e.task_page_search_result_1_native_text, "Elder")