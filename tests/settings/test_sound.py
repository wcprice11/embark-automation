from glob import escape
from tests.embark_tests import VisualEmbarkStageTest
from selenium.webdriver.common.keys import Keys

class TestSound(VisualEmbarkStageTest):
    def test_sound(self):
        e = self.elements
        self.login("spanish")
        self.click(e.whats_new_card_close_button)
        self.click(e.settings_button)
        self.click(e.sound_effects_toggle)
        toggle = self.get_element(e.sound_effects_toggle)
        isChecked = toggle.get_attribute("aria-checked")
        self.validate_text(isChecked, "false")

        # If you can figure out how to really make sure sound didn't happen, this block of code will help
        # elem = self.get_element(e.body)
        # elem.send_keys(Keys.ESCAPE)
        # # self.click(e.basic_tab)
        # self.click(e.alphabet_learn_card)
        # self.click(e.lesson_card)
        # self.click(e.lesson_practice_button)
        # self.click(e.lesson_practice_fill_in_blank)
        # self.click(e.lesson_discover_flashcards_start)
        # self.fill(e.lesson_practice_input, "r")
        # audio = self.get_element(e.audio)
        # self.click(e.lesson_practice_check)

        