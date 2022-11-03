# Search
from tests.embark_test_classes import VisualEmbarkStageTest

class TestAboutHyperlinks(VisualEmbarkStageTest):
    def test_search_page(self):
        e = self.elements
        self.login("spanish")
        self.wait_for_element_to_be_clickable(e.whats_new_card_close_button)
        self.click(e.whats_new_card_close_button)
        self.validate_element_text( e.search_button,            "Search")
        self.click(                 e.search_button)
        self.wait_for_element_to_be_clickable( e.tip_pop_up_close)
        self.validate_element_text( e.tip_pop_up,               "Search empowers you to find specific words, phrases, and resources.") 
        self.click(                 e.tip_pop_up_close)
        self.validate_element_text( e.search_page_words_tab, "Words")
        self.validate_element_text( e.search_page_phrases_tab, "Phrases")
        self.validate_element_text( e.search_page_resources_tab, "Resources")
        self.fill(                  e.search_bar, "Absolute gobblty gook", enter=True)
        self.wait_for_text_in_element( e.search_no_results_message, "No matches found.")
        self.click(                 e.search_page_phrases_tab)
        self.wait_for_text_in_element( e.search_no_results_message, "No matches found.")
        self.click(                 e.search_page_resources_tab)
        self.wait_for_text_in_element( e.search_no_results_message, "No matches found.")
        self.click(                 e.search_page_words_tab)
        self.wait_for_text_in_element( e.search_no_results_message, "No matches found.")
        self.fill(                  e.search_bar, "Jesus", enter=True)
        self.wait_for_element_to_be_clickable( e.search_first_result)
        self.validate_element_text( e.search_first_result, "Jesús\nJesus")
        # FIX ME shouldn't these results link somewhere?
        self.click(                 e.search_page_phrases_tab)
        self.wait_for_element_to_be_clickable( e.search_first_result)
        self.validate_element_text( e.search_first_result, "Amo a Jesucristo.\nI love Jesus Christ.")
        self.click(                 e.search_page_resources_tab)
        self.wait_for_element_to_be_clickable( e.search_first_result)
        self.validate_element_text( e.search_first_result, "Teach about Jesus Christ")
        self.click(                 e.search_first_result)
        self.wait_for_text_in_url( "tall.global/embark/#/home/mediaItem/")
