from tests.embark_tests import VisualEmbarkProdTest

class TestMarshalleeseLoads(VisualEmbarkProdTest):
    def test_marshalleese(self):
        e = self.elements
        self.login("marshallese")
        self.wait_for_text_in_element(self.e.whats_new_card_close_button, "Close")
        self.click(e.whats_new_card_close_button)
        pass
