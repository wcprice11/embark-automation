from tests.embark_tests import *

class TestStageSettings(EmbarkStageTest):
    def test_stage_settings_validation(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(s.login())
        s.click(e.i_want_to_learn)
        s.click(e.learn_spanish)
        s.click(e.language_submit)
        s.click(e.whats_new_card_close_button)
        s.click(e.home_button)
        self.validate_url_contains(u.BLANK_HOME)

        elem = s.find(e.settings_button)
        self.validate_text(elem.text, "Settings")
        s.click(e.settings_button)

        elem = s.find(e.log_out_button)
        self.validate_text(elem.text, "Log out")
        elem = s.find(e.languages_button)
        self.validate_text_contains(elem.text, "Languages")
        elem = s.find(e.sound_effects)
        self.validate_text(elem.text, "Sound Effects")
        elem = s.find(e.contact_us_button)
        self.validate_text(elem.text, "Contact us")
        elem = s.find(e.troubleshooting_button)
        self.validate_text(elem.text, "Troubleshooting")
        elem = s.find(e.whats_new_button)
        self.validate_text(elem.text, "What's new?")
        elem = s.find(e.about_button)
        self.validate_text(elem.text, "About")
