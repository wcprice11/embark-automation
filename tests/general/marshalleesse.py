from tests.embark_test_classes import EmbarkProdTest

class TestMarshalleseLoads(EmbarkProdTest):
    def test_marshallese(self):
        e = self.elements
        self.login("marshallese")
        self.wait_for_text_in_element(self.e.whats_new_card_close_button, "Close")
        self.click(e.whats_new_card_close_button)
        pass
