from tests.embark_tests import EmbarkStageTest
class TestRecordAudio(EmbarkStageTest):
    def test_record_audio(self):
        e = self.elements
        self.login("spanish")
        self.wait_for_text_in_element(e.whats_new_card_close_button, "Close")
        self.click(e.whats_new_card_close_button)
        # Check if in recommended
        self.find(e.recommended_meet_someone_lesson)
        self.validate_element_text(e.recommended_meet_someone_lesson, "Meet Someone\nBasic")
        self.click(e.recommended_meet_someone_lesson)
        self.wait_for_text_in_element(e.page_title, "Meet Someone")
        self.validate_element_text(e.lesson_section_title, "Essentials")
        self.validate_element_text(e.lesson_card, "Vocabulary")
        self.click(e.lesson_card)
        self.wait_for_element_to_be_clickable(e.lesson_discover_button)
        self.click(e.lesson_discover_button)
        self.click(e.start_button)
        self.click(e.vocab_discover_record)
        self.find(e.vocab_discover_recording)
        self.click(e.vocab_discover_recording)
        self.find(e.vocab_discover_play_recording)
        self.find(e.vocab_discover_re_record)