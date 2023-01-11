from tests.embark_test_classes import EmbarkRCTest, EmbarkProdTest

class TestLogoutRC(EmbarkRCTest):
    def test_logout_button(self):
        e = self.elements
        self.login("french")
        self.wait_for_element_to_be_clickable(e.whats_new_card_close_button)
        self.click(e.whats_new_card_close_button)
        self.click(e.settings_button)
        elem = self.get_element(e.log_out_button)
        self.validate_text(elem.text, "Log out")
        self.click(e.log_out_button)
        self.wait_for_text_in_url("churchofjesuschrist")


class TestLogoutProd(EmbarkProdTest):
    def test_logout_button(self):
        e = self.elements
        self.login("french")
        self.wait_for_element_to_be_clickable(e.whats_new_card_close_button)
        self.click(e.whats_new_card_close_button)
        self.click(e.settings_button)
        elem = self.get_element(e.log_out_button)
        self.validate_text(elem.text, "Log out")
        self.click(e.log_out_button)
        self.wait_for_text_in_url("churchofjesuschrist")

