from tests.embark_test_classes import VisualEmbarkStageTest
from sessions.embark_user import test_user_02

# From card https://trello.com/c/n9G3Lf42/1310-deleting-or-adding-topics-quickly-has-a-chance-to-crash-add-words-completely-ld1310

class TestAddTopics(VisualEmbarkStageTest):

    def test_add_topics(self):
        oneDeleted = False
        e = self.elements
        self.load_user(test_user_02)
        self.login("spanish")
        self.wait_for_text_in_element(e.whats_new_card_close_button, "Close")
        self.click(e.whats_new_card_close_button)

        self.click(e.my_added_words)
        
        # Deleting topics
        no_added_topics_text = self.get_element(e.added_topics_absent_text).text
        self.click(e.added_words_edit)
        while no_added_topics_text != "You have no added topics":
            oneDeleted = True
            no_added_topics_text = self.get_element(e.added_topics_absent_text).text
            if no_added_topics_text == "You have no added topics.":
                break
            self.click(e.added_words_delete)
            self.click(e.added_words_confirm_delete)
            no_added_topics_text = self.get_element(e.added_topics_absent_text).text

        if oneDeleted:
            self.driver.refresh()
        oneDeleted = False

        for i in range(20):
            self.click(e.add_topic)
            self.fill(e.add_topic_title, "Test Topic " + str(i))
            self.fill(e.add_topic_add_word_native, "Test Word " + str(i))
            self.fill(e.add_topic_add_word_target, "Test Translation " + str(i))
            self.click(e.add_topic_done_button)
            self.click(e.added_topic_task_page_back_button)

        self.click(e.added_words_edit)
        # Deleting topics
        no_added_topics_text = self.get_element(e.added_topics_absent_text).text
        while no_added_topics_text != "You have no added topics.":
            no_added_topics_text = self.get_element(e.added_topics_absent_text).text
            if no_added_topics_text == "You have no added topics.":
                break
            self.click(e.added_words_delete)
            self.click(e.added_words_confirm_delete)
            no_added_topics_text = self.get_element(e.added_topics_absent_text).text
        
        if oneDeleted:
            self.driver.refresh()