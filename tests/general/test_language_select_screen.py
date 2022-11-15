from tests.embark_test_classes import EmbarkDevTest, EmbarkProdTest, EmbarkRCTest, EmbarkStageTest

class TestProdLanguageSelectScreen(EmbarkProdTest):
    def test_prod_language_select_screen(self):
        e = self.elements
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.find(e.learn_english)
        self.find(e.learn_french)
        self.find(e.learn_korean)
        self.find(e.learn_spanish)
        self.find(e.learn_vietnamese)
        elem = self.get_element(e.learn_vietnamese)
        self.validate_text_contains(elem.text, "Vietnamese") # checking the last verifies no single change in the middle
        self.click(e.learn_vietnamese)
        self.click(e.native_language)
        self.find(e.native_english)
        self.find(e.native_french)
        self.find(e.native_korean)
        self.find(e.native_spanish)
        self.find(e.native_vietnamese)
        self.click(e.native_korean)
        self.click(e.i_want_to_learn)
        self.find(e.learn_french)
        self.find(e.learn_korean)
        self.find(e.learn_vietnamese)
        self.find(e.learn_spanish)
        self.click(e.learn_spanish)
        self.click(e.native_language)
        self.find(e.native_vietnamese)
        self.find(e.native_french)
        self.find(e.native_korean)
        self.find(e.native_spanish)
        self.find(e.native_english)
        self.click(e.native_english)

    def test_prod_language_select_screen_load_core_language(self):
        e = self.elements
        self.assertTrue(self.login("spanish"))
        self.click(e.for_you_tab)
        self.validate_text_contains(self.get_url(), self.urls.BLANK_HOME)
        
    def test_prod_language_select_screen_load_non_core_language(self):
        e = self.elements
        self.assertTrue(self.login("korean"))
        self.click(e.for_you_tab)
        self.validate_text_contains(self.get_url(), self.urls.BLANK_HOME)

class TestStageLanguageSelectScreen(EmbarkStageTest):
    def test_stage_language_select_screen(self):
        e = self.elements
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.find(e.learn_english)
        self.find(e.learn_french)
        self.find(e.learn_korean)
        self.find(e.learn_spanish)
        self.find(e.learn_vietnamese)
        elem = self.get_element(e.learn_vietnamese)
        self.validate_text_contains(elem.text, "Vietnamese") # checking the last verifies no single change in the middle
        self.click(e.learn_vietnamese)
        self.click(e.native_language)
        self.find(e.native_english)
        self.find(e.native_french)
        self.find(e.native_korean)
        self.find(e.native_spanish)
        self.find(e.native_vietnamese)
        self.click(e.native_korean)
        self.click(e.i_want_to_learn)
        self.find(e.learn_french)
        self.find(e.learn_korean)
        self.find(e.learn_vietnamese)
        self.find(e.learn_spanish)
        self.click(e.learn_spanish)
        self.click(e.native_language)
        self.find(e.native_vietnamese)
        self.find(e.native_french)
        self.find(e.native_korean)
        self.find(e.native_spanish)
        self.find(e.native_english)
        self.click(e.native_english)

    def test_stage_language_select_screen_load_core_language(self):
        e = self.elements
        self.assertTrue(self.login("spanish"))
        self.click(e.for_you_tab)
        self.validate_text_contains(self.get_url(), self.urls.BLANK_HOME)
        
    def test_stage_language_select_screen_load_non_core_language(self):
        e = self.elements
        self.assertTrue(self.login("korean"))
        self.click(e.for_you_tab)
        self.validate_text_contains(self.get_url(), self.urls.BLANK_HOME)

class TestRCLanguageSelectScreen(EmbarkRCTest):
    def test_rc_language_select_screen(self):
        e = self.elements
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.find(e.learn_english)
        self.find(e.learn_french)
        self.find(e.learn_korean)
        self.find(e.learn_spanish)
        self.find(e.learn_vietnamese)
        elem = self.get_element(e.learn_vietnamese)
        self.validate_text_contains(elem.text, "Vietnamese") # checking the last verifies no single change in the middle
        self.click(e.learn_vietnamese)
        self.click(e.native_language)
        self.find(e.native_english)
        self.find(e.native_french)
        self.find(e.native_korean)
        self.find(e.native_spanish)
        self.find(e.native_vietnamese)
        self.click(e.native_korean)
        self.click(e.i_want_to_learn)
        self.find(e.learn_french)
        self.find(e.learn_korean)
        self.find(e.learn_vietnamese)
        self.find(e.learn_spanish)
        self.click(e.learn_spanish)
        self.click(e.native_language)
        self.find(e.native_vietnamese)
        self.find(e.native_french)
        self.find(e.native_korean)
        self.find(e.native_spanish)
        self.find(e.native_english)
        self.click(e.native_english)

    def test_rc_language_select_screen_load_core_language(self):
        e = self.elements
        self.assertTrue(self.login("spanish"))
        self.click(e.for_you_tab)
        self.validate_text_contains(self.get_url(), self.urls.BLANK_HOME)
        
    def test_rc_language_select_screen_load_non_core_language(self):
        e = self.elements
        self.assertTrue(self.login("korean"))
        self.click(e.for_you_tab)
        self.validate_text_contains(self.get_url(), self.urls.BLANK_HOME)

class TestDevLanguageSelectScreen(EmbarkDevTest):
    def test_dev_language_select_screen(self):
        e = self.elements
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.find(e.learn_english)
        self.find(e.learn_french)
        self.find(e.learn_korean)
        self.find(e.learn_spanish)
        self.find(e.learn_vietnamese)
        elem = self.get_element(e.learn_vietnamese)
        self.validate_text_contains(elem.text, "Vietnamese") # checking the last verifies no single change in the middle
        self.click(e.learn_vietnamese)
        self.click(e.native_language)
        self.find(e.native_english)
        self.find(e.native_french)
        self.find(e.native_korean)
        self.find(e.native_spanish)
        self.find(e.native_vietnamese)
        self.click(e.native_korean)
        self.click(e.i_want_to_learn)
        self.find(e.learn_french)
        self.find(e.learn_korean)
        self.find(e.learn_vietnamese)
        self.find(e.learn_spanish)
        self.click(e.learn_spanish)
        self.click(e.native_language)
        self.find(e.native_vietnamese)
        self.find(e.native_french)
        self.find(e.native_korean)
        self.find(e.native_spanish)
        self.find(e.native_english)
        self.click(e.native_english)

    def test_dev_language_select_screen_load_core_language(self):
        e = self.elements
        self.assertTrue(self.login("spanish"))
        self.click(self.elements.whats_new_card_close_button)
        self.click(e.for_you_tab)
        self.validate_text_contains(self.get_url(), self.urls.BLANK_HOME)
        
    def test_dev_language_select_screen_load_non_core_language(self):
        e = self.elements
        self.assertTrue(self.login("korean"))
        self.click(self.elements.whats_new_card_close_button)
        self.click(e.for_you_tab)
        self.validate_text_contains(self.get_url(), self.urls.BLANK_HOME)
