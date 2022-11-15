from tests.embark_test_classes import EmbarkStageTest, EmbarkProdTest

class TestLogoutStage(EmbarkStageTest):
    def test_logout_button(self):
        e = self.elements
        self.login("french")
        self.find(e.whats_new_card_close_button)
        self.click(e.whats_new_card_close_button)
        self.click(e.settings_button)
        elem = self.get_element(e.log_out_button)
        self.validate_text(elem.text, "Log out")
        self.click(e.log_out_button)
        self.find(e.church_site_header)
        self.get(self.urls.LOGIN)
        self.assertEqual(self.urls.LOGIN, self.get_url())

class TestLogoutProd(EmbarkProdTest):
    def test_logout_button(self):
        e = self.elements
        self.login("french")
        self.find(e.whats_new_card_close_button)
        self.click(e.whats_new_card_close_button)
        self.click(e.settings_button)
        elem = self.get_element(e.log_out_button)
        self.validate_text(elem.text, "Log out")
        self.click(e.log_out_button)
        self.find(e.church_site_header)
        self.get(self.urls.LOGIN)
        self.assertEqual(self.urls.LOGIN, self.get_url())

