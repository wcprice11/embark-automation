from tests.embark_test_classes import VisualEmbarkStageTest
from sessions.embark_user import test_user_02
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import string
import re

# Currently, this test just checks unscramble in the Practice section. Due to a but, unscramble currently doesn't show up in 

class TestVocabSpacedReviewAlgorithm(VisualEmbarkStageTest):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName)
        self.word_pairs = {"church":"iglesia", "companion (male)":"compañero", "companion (female)":"compañera", "city":"ciudad", "Elder":"Élder (misionero)", "day":"día", "Hello.": "Hola."}
        self.word_pairs["My name is _____."] = "me llamo _____"
        self.word_pairs["How are you doing?"] = "cómo le va?"
        self.word_pairs["What is your name?"] = "cuál es su nombre"
        self.word_pairs["Where are you from?"] = "¿de dónde es?"
        self.word_pairs["I am from _____."] = "yo soy de _____"
        self.word_pairs["I like to play basketball."] = "me gusta jugar baloncesto."
        self.word_pairs["I am Sister _____."] = "yo soy la hermana _____"
        self.word_pairs["The Church of Jesus Christ of Latter-day Saints"] = "La Iglesia de Jesucristo de los Santos de los Últimos Días"
        self.word_pairs["I am Elder _____."] = "yo soy el Élder _____"
        self.word_pairs["We are missionaries of the Church of Jesus Christ of Latter-day Saints."] = "Somos misioneros de La Iglesia de Jesucristo de los Santos de los Últimos Días"
        self.word_pairs["What do you like to do?"] = "qué le gusta hacer"        
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
        self.click(e.lesson_card_phrases)
        self.wait_for_element_to_be_clickable(e.lesson_discover_button)

        self.markWords("")

        self.click(e.lesson_practice_button)
        self.click(e.lesson_practice_unscramble)
        self.click(e.start_button)

        done = False

        while not done:
            translation = self.word_pairs[self.get_element(e.lesson_unscramble_prompt).text]
            translation = re.sub(r'[^\w\s]', '', translation)
            translation = translation.lower().split(" ")
            while '' in translation:
                translation.remove('')
            numChips = len(translation)
            
            for word in translation:
                wordlist = []
                base_sel = "app-unscramble-activity>div>div>ion-card:nth-of-type(2)>ion-card-content>div:nth-of-type("
                base_sel_2 = ")>span"
                found = False
                for j in range(numChips):
                    if not found:
                        sel = (By.CSS_SELECTOR, base_sel + str(j+1) + base_sel_2, "Chip number " + str(j+1) + " in unscramble")
                        candidate = self.get_element(sel).text.lower()
                        wordlist.append(candidate)
                        if candidate == word:
                            self.click(sel)
                            found = True
                            numChips -= 1

                if not found:
                    self.fail("Couldn't find word: " + word + ". Candidate list: " + str(wordlist))
            self.click(e.lesson_unscramble_check_button)
            self.click(e.lesson_unscramble_check_button)

            # self.fail(str(self.get_element(e.lesson_unscramble_prompt).size))
            if self.get_element(e.lesson_unscramble_prompt) is None:
                done = True

        self.click(e.pick_activity_back_button)
        self.click(e.pick_activity_back_button)
        self.markWords("")


    def markWords(self, target):
        if target == "mastered":
            target_name = "checkmark-done-circle"
        elif target == "discovered":
            target_name = "checkmark-circle-outline"
        else:
            target_name = "ellipse-outline"
        base_sel_1 = "app-task-study-list>ion-content>div>div>div>app-concept-list:nth-of-type(2)>ion-card>ion-item:nth-of-type("
        base_sel_2 = ")>ion-icon:nth-of-type(3)"
        base_label = "Discovered button in vocab list "
        for i in range(6):
            sel = (By.CSS_SELECTOR, base_sel_1 + str(i+2) + base_sel_2, base_label + str(i+1))
            name = self.get_element(sel).get_attribute("name")
            while name != target_name:
                self.click(sel)
                name = self.get_element(sel).get_attribute("name")