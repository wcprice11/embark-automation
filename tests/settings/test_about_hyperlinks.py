from tests.embark_tests import EmbarkStageTest

class TestAboutHyperlinks(EmbarkStageTest):
    def test_about_hyperlinks(self):
        e = self.elements
        self.login("spanish")
        self.click(e.whats_new_card_close_button)
        self.click(e.settings_button)
        self.click(e.about_button)
        check = self.get_element(e.about_page_hyperlinks_privacy_notice)
        self.validate_text(check.text, "Privacy Notice")
        check = self.get_element(e.about_page_hyperlinks_terms_of_use)
        self.validate_text(check.text, "Terms of Use")
        check = self.get_element(e.about_page_hyperlinks_acknowledgements)
        self.validate_text(check.text, "Acknowledgements")
        self.click(e.about_page_hyperlinks_privacy_notice)