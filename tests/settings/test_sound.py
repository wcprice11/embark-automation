from tests.embark_tests import VisualEmbarkStageTest

class TestSound(VisualEmbarkStageTest):
    def test_sound(self):
        e = self.elements
        self.login("spanish")
        self.click(e.whats_new_card_close_button)
        self.click(e.settings_button)
        self.click(e.sound_effects_toggle)