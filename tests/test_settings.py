from tests.embark_tests import *


class TestStageSettings(EmbarkStageTest):

    def test_stage_settings_validation(self):
        u = self.urls
        e = self.elements
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.click(e.learn_spanish)
        self.click(e.language_submit)
        self.click(e.whats_new_card_close_button)
        self.click(e.home_button)
        self.validate_url_contains(u.BLANK_HOME)

        elem = self.get_element(e.settings_button)
        self.validate_text(elem.text, "Settings")
        self.click(e.settings_button)

        elem = self.get_element(e.log_out_button)
        self.validate_text(elem.text, "Log out")
        elem = self.get_element(e.languages_button)
        self.validate_text_contains(elem.text, "Languages")
        elem = self.get_element(e.sound_effects)
        self.validate_text(elem.text, "Sound Effects")
        elem = self.get_element(e.contact_us_button)
        self.validate_text(elem.text, "Contact us")
        elem = self.get_element(e.troubleshooting_button)
        self.validate_text(elem.text, "Troubleshooting")
        elem = self.get_element(e.whats_new_button)
        self.validate_text(elem.text, "What's new?")
        elem = self.get_element(e.about_button)
        self.validate_text(elem.text, "About")

    def test_stage_logout(self):
        self.assertTrue(self.login("spanish"))
        self.click(self.elements.whats_new_card_close_button)



