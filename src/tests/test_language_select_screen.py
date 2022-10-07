import unittest
from time import sleep
from sessions.embark_session import Session
from sessions.embark_branch import web_prod, web_dev, web_rc, web_stage

class TestProdLanguageSelectScreen(unittest.TestCase):
    def setUp(self) -> None:
        self.session = Session()
        self.session.start()

    def test_prod_language_select_screen(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(s.login())
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_english))
        self.assertTrue(s.find(e.learn_french))
        self.assertTrue(s.find(e.learn_korean))
        self.assertTrue(s.find(e.learn_spanish))
        self.assertTrue(s.find(e.learn_vietnamese))
        s.click(e.learn_vietnamese)
        s.click(e.native_language)
        self.assertTrue(s.find(e.native_english))
        self.assertTrue(s.find(e.native_french))
        self.assertTrue(s.find(e.native_korean))
        self.assertTrue(s.find(e.native_spanish))
        self.assertTrue(s.find(e.native_vietnamese))
        s.click(e.native_korean)
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_french))
        self.assertTrue(s.find(e.learn_korean))
        self.assertTrue(s.find(e.learn_vietnamese))
        self.assertTrue(s.find(e.learn_spanish))
        s.click(e.learn_spanish)
        s.click(e.native_language)
        self.assertTrue(s.find(e.native_vietnamese))
        self.assertTrue(s.find(e.native_french))
        self.assertTrue(s.find(e.native_korean))
        self.assertTrue(s.find(e.native_spanish))
        self.assertTrue(s.find(e.native_english))
        s.click(e.native_english)
        
    def test_prod_language_select_screen_load_core_language(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(s.login())
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_spanish))
        s.click(e.learn_spanish)
        s.click(e.language_submit)
        s.click(e.for_you_tab)
        self.assertTrue(u.BLANK_HOME[0:35] in s.get_url(), "Unexpected URL")
        
    def test_prod_language_select_screen_load_non_core_language(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(s.login())
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_spanish))
        s.click(e.learn_korean)
        s.click(e.language_submit)
        s.click(e.for_you_tab)
        self.assertTrue(u.BLANK_HOME[0:35] in s.get_url(), "Unexpected URL")



    def tearDown(self) -> None:
        self.session.save_screenshot(f"./report/{self.id()}.png")
        self.session.quit()

class TestStageLanguageSelectScreen(unittest.TestCase):
    def setUp(self) -> None:
        self.session = Session(branch=web_stage)
        self.session.start()

    def test_prod_language_select_screen(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(s.login())
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_english))
        self.assertTrue(s.find(e.learn_french))
        self.assertTrue(s.find(e.learn_korean))
        self.assertTrue(s.find(e.learn_spanish))
        self.assertTrue(s.find(e.learn_vietnamese))
        s.click(e.learn_vietnamese)
        s.click(e.native_language)
        self.assertTrue(s.find(e.native_english))
        self.assertTrue(s.find(e.native_french))
        self.assertTrue(s.find(e.native_korean))
        self.assertTrue(s.find(e.native_spanish))
        self.assertTrue(s.find(e.native_vietnamese))
        s.click(e.native_korean)
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_french))
        self.assertTrue(s.find(e.learn_korean))
        self.assertTrue(s.find(e.learn_vietnamese))
        self.assertTrue(s.find(e.learn_spanish))
        s.click(e.learn_spanish)
        s.click(e.native_language)
        self.assertTrue(s.find(e.native_vietnamese))
        self.assertTrue(s.find(e.native_french))
        self.assertTrue(s.find(e.native_korean))
        self.assertTrue(s.find(e.native_spanish))
        self.assertTrue(s.find(e.native_english))
        s.click(e.native_english)
        
    def test_prod_language_select_screen_load_core_language(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(s.login())
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_spanish))
        s.click(e.learn_spanish)
        s.click(e.language_submit)
        s.click(e.for_you_tab)
        self.assertTrue(u.BLANK_HOME[0:35] in s.get_url(), "Unexpected URL")
        
    def test_prod_language_select_screen_load_non_core_language(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(s.login())
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_spanish))
        s.click(e.learn_korean)
        s.click(e.language_submit)
        s.click(e.for_you_tab)
        self.assertTrue(u.BLANK_HOME[0:35] in s.get_url(), "Unexpected URL")



    def tearDown(self) -> None:
        self.session.save_screenshot(f"./report/{self.id()}.png")
        self.session.quit()

class TestRCLanguageSelectScreen(unittest.TestCase):
    def setUp(self) -> None:
        self.session = Session(branch=web_rc)
        self.session.start()

    def test_prod_language_select_screen(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(s.login())
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_english))
        self.assertTrue(s.find(e.learn_french))
        self.assertTrue(s.find(e.learn_korean))
        self.assertTrue(s.find(e.learn_spanish))
        self.assertTrue(s.find(e.learn_vietnamese))
        s.click(e.learn_vietnamese)
        s.click(e.native_language)
        self.assertTrue(s.find(e.native_english))
        self.assertTrue(s.find(e.native_french))
        self.assertTrue(s.find(e.native_korean))
        self.assertTrue(s.find(e.native_spanish))
        self.assertTrue(s.find(e.native_vietnamese))
        s.click(e.native_korean)
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_french))
        self.assertTrue(s.find(e.learn_korean))
        self.assertTrue(s.find(e.learn_vietnamese))
        self.assertTrue(s.find(e.learn_spanish))
        s.click(e.learn_spanish)
        s.click(e.native_language)
        self.assertTrue(s.find(e.native_vietnamese))
        self.assertTrue(s.find(e.native_french))
        self.assertTrue(s.find(e.native_korean))
        self.assertTrue(s.find(e.native_spanish))
        self.assertTrue(s.find(e.native_english))
        s.click(e.native_english)
        
    def test_prod_language_select_screen_load_core_language(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(s.login())
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_spanish))
        s.click(e.learn_spanish)
        s.click(e.language_submit)
        s.click(e.for_you_tab)
        self.assertTrue(u.BLANK_HOME[0:35] in s.get_url(), "Unexpected URL")
        
    def test_prod_language_select_screen_load_non_core_language(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(s.login())
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_spanish))
        s.click(e.learn_korean)
        s.click(e.language_submit)
        s.click(e.for_you_tab)
        self.assertTrue(u.BLANK_HOME[0:35] in s.get_url(), "Unexpected URL")



    def tearDown(self) -> None:
        self.session.save_screenshot(f"./report/{self.id()}.png")
        self.session.quit()

class TestDevLanguageSelectScreen(unittest.TestCase):
    def setUp(self) -> None:
        self.session = Session(branch=web_dev)
        self.session.start()

    def test_prod_language_select_screen(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(s.login())
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_english))
        self.assertTrue(s.find(e.learn_french))
        self.assertTrue(s.find(e.learn_korean))
        self.assertTrue(s.find(e.learn_spanish))
        self.assertTrue(s.find(e.learn_vietnamese))
        s.click(e.learn_vietnamese)
        s.click(e.native_language)
        self.assertTrue(s.find(e.native_english))
        self.assertTrue(s.find(e.native_french))
        self.assertTrue(s.find(e.native_korean))
        self.assertTrue(s.find(e.native_spanish))
        self.assertTrue(s.find(e.native_vietnamese))
        s.click(e.native_korean)
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_french))
        self.assertTrue(s.find(e.learn_korean))
        self.assertTrue(s.find(e.learn_vietnamese))
        self.assertTrue(s.find(e.learn_spanish))
        s.click(e.learn_spanish)
        s.click(e.native_language)
        self.assertTrue(s.find(e.native_vietnamese))
        self.assertTrue(s.find(e.native_french))
        self.assertTrue(s.find(e.native_korean))
        self.assertTrue(s.find(e.native_spanish))
        self.assertTrue(s.find(e.native_english))
        s.click(e.native_english)
        
    def test_prod_language_select_screen_load_core_language(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(s.login())
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_spanish))
        s.click(e.learn_spanish)
        s.click(e.language_submit)
        s.click(e.for_you_tab)
        self.assertTrue(u.BLANK_HOME[0:35] in s.get_url(), "Unexpected URL")
        
    def test_prod_language_select_screen_load_non_core_language(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(s.login())
        s.click(e.i_want_to_learn)
        self.assertTrue(s.find(e.learn_spanish))
        s.click(e.learn_korean)
        s.click(e.language_submit)
        s.click(e.for_you_tab)
        self.assertTrue(u.BLANK_HOME[0:35] in s.get_url(), "Unexpected URL")



    def tearDown(self) -> None:
        self.session.save_screenshot(f"./report/{self.id()}.png")
        self.session.quit()
