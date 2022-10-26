from tests.embark_tests import VisualEmbarkProdTest

class TestMarshalleseLoads(VisualEmbarkProdTest):
    def test_marshallese(self):
        e = self.elements
        self.login("marshallese")
        self.wait_for_text_in_element(self.e.whats_new_card_close_button, "Close")
        self.click(e.whats_new_card_close_button)
        pass
