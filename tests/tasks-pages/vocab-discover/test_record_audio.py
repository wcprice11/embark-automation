from tests.embark_test_classes import EmbarkRCTest

'''
This test currently:
1. Navigates to Meet Someone > Vocabulary
2. Goes to Flashcards
3. On the first flashcard, clicks Record and checks that the icon is correct
4. Clicks it again and checks that the icon is correct

Ideas for future use:
1. Find a way to actually detect audio/detect a file being attached to the Audio component. 
Detecting actual audio playing is one of Selenium's big drawbacks, so we may use a different
tool in the future to accomplish this.
'''

class TestRecordAudio(EmbarkRCTest):
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