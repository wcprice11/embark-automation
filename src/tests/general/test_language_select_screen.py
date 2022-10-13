import unittest
from time import sleep
from sessions.embark_session import SessionMixIn
from sessions.embark_branch import web_prod, web_dev, web_rc, web_stage
from tests.embark_tests import EmbarkDevTest, EmbarkProdTest, EmbarkRCTest, EmbarkStageTest

class TestProdLanguageSelectScreen(EmbarkProdTest):
    def test_prod_language_select_screen(self):
        e = self.elements
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.assertTrue(self.find(e.learn_english))
        self.assertTrue(self.find(e.learn_french))
        self.assertTrue(self.find(e.learn_korean))
        self.assertTrue(self.find(e.learn_spanish))
        self.assertTrue(self.find(e.learn_vietnamese))
        self.click(e.learn_vietnamese)
        self.click(e.native_language)
        self.assertTrue(self.find(e.native_english))
        self.assertTrue(self.find(e.native_french))
        self.assertTrue(self.find(e.native_korean))
        self.assertTrue(self.find(e.native_spanish))
        self.assertTrue(self.find(e.native_vietnamese))
        self.click(e.native_korean)
        self.click(e.i_want_to_learn)
        self.assertTrue(self.find(e.learn_french))
        self.assertTrue(self.find(e.learn_korean))
        self.assertTrue(self.find(e.learn_vietnamese))
        self.assertTrue(self.find(e.learn_spanish))
        self.click(e.learn_spanish)
        self.click(e.native_language)
        self.assertTrue(self.find(e.native_vietnamese))
        self.assertTrue(self.find(e.native_french))
        self.assertTrue(self.find(e.native_korean))
        self.assertTrue(self.find(e.native_spanish))
        self.assertTrue(self.find(e.native_english))
        self.click(e.native_english)
        
    def test_prod_language_select_screen_load_core_language(self):
        e = self.elements
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.assertTrue(self.find(e.learn_spanish))
        self.click(e.learn_spanish)
        self.click(e.language_submit)
        self.click(e.for_you_tab)
        self.assertTrue(self.urls.BLANK_HOME[0:35] in self.get_url(), "Unexpected URL")
        
    def test_prod_language_select_screen_load_non_core_language(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.assertTrue(self.find(e.learn_spanish))
        self.click(e.learn_korean)
        self.click(e.language_submit)
        self.click(e.for_you_tab)
        self.assertTrue(u.BLANK_HOME[0:35] in s.get_url(), "Unexpected URL")


class TestStageLanguageSelectScreen(EmbarkStageTest):
    def test_prod_language_select_screen(self):
        e = self.elements
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.find(e.learn_english)
        self.find(e.learn_french)
        self.find(e.learn_korean)
        self.find(e.learn_spanish)
        self.find(e.learn_vietnamese)
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
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.assertTrue(self.find(e.learn_spanish))
        self.click(e.learn_spanish)
        self.click(e.language_submit)
        self.click(e.for_you_tab)
        self.assertTrue(self.urls.BLANK_HOME[0:35] in self.get_url(), "Unexpected URL")
        
    def test_prod_language_select_screen_load_non_core_language(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.assertTrue(self.find(e.learn_spanish))
        self.click(e.learn_korean)
        self.click(e.language_submit)
        self.click(e.for_you_tab)
        self.assertTrue(u.BLANK_HOME[0:35] in s.get_url(), "Unexpected URL")


class TestRCLanguageSelectScreen(EmbarkRCTest):
    def test_prod_language_select_screen(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.assertTrue(self.find(e.learn_english))
        self.assertTrue(self.find(e.learn_french))
        self.assertTrue(self.find(e.learn_korean))
        self.assertTrue(self.find(e.learn_spanish))
        self.assertTrue(self.find(e.learn_vietnamese))
        self.click(e.learn_vietnamese)
        self.click(e.native_language)
        self.assertTrue(self.find(e.native_english))
        self.assertTrue(self.find(e.native_french))
        self.assertTrue(self.find(e.native_korean))
        self.assertTrue(self.find(e.native_spanish))
        self.assertTrue(self.find(e.native_vietnamese))
        self.click(e.native_korean)
        self.click(e.i_want_to_learn)
        self.assertTrue(self.find(e.learn_french))
        self.assertTrue(self.find(e.learn_korean))
        self.assertTrue(self.find(e.learn_vietnamese))
        self.assertTrue(self.find(e.learn_spanish))
        self.click(e.learn_spanish)
        self.click(e.native_language)
        self.assertTrue(self.find(e.native_vietnamese))
        self.assertTrue(self.find(e.native_french))
        self.assertTrue(self.find(e.native_korean))
        self.assertTrue(self.find(e.native_spanish))
        self.assertTrue(self.find(e.native_english))
        self.click(e.native_english)
        
    def test_prod_language_select_screen_load_core_language(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.assertTrue(self.find(e.learn_spanish))
        self.click(e.learn_spanish)
        self.click(e.language_submit)
        self.click(e.for_you_tab)
        self.assertTrue(u.BLANK_HOME[0:35] in s.get_url(), "Unexpected URL")
        
    def test_prod_language_select_screen_load_non_core_language(self):
        s = self.session
        u = s.URLs
        e = s.elements
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.assertTrue(self.find(e.learn_spanish))
        self.click(e.learn_korean)
        self.click(e.language_submit)
        self.click(e.for_you_tab)
        self.assertTrue(u.BLANK_HOME[0:35] in s.get_url(), "Unexpected URL")

class TestDevLanguageSelectScreen(EmbarkDevTest):
    def test_prod_language_select_screen(self):
        e = self.elements
        self.assertTrue(self.login())
        self.click(e.i_want_to_learn)
        self.assertTrue(self.find(e.learn_english))
        self.assertTrue(self.find(e.learn_french))
        self.assertTrue(self.find(e.learn_korean))
        self.assertTrue(self.find(e.learn_spanish))
        self.assertTrue(self.find(e.learn_vietnamese))
        self.click(e.learn_vietnamese)
        self.click(e.native_language)
        self.assertTrue(self.find(e.native_english))
        self.assertTrue(self.find(e.native_french))
        self.assertTrue(self.find(e.native_korean))
        self.assertTrue(self.find(e.native_spanish))
        self.assertTrue(self.find(e.native_vietnamese))
        self.click(e.native_korean)
        self.click(e.i_want_to_learn)
        self.assertTrue(self.find(e.learn_french))
        self.assertTrue(self.find(e.learn_korean))
        self.assertTrue(self.find(e.learn_vietnamese))
        self.assertTrue(self.find(e.learn_spanish))
        self.click(e.learn_spanish)
        self.click(e.native_language)
        self.assertTrue(self.find(e.native_vietnamese))
        self.assertTrue(self.find(e.native_french))
        self.assertTrue(self.find(e.native_korean))
        self.assertTrue(self.find(e.native_spanish))
        self.assertTrue(self.find(e.native_english))
        self.click(e.native_english)
        
    def test_prod_language_select_screen_load_core_language(self):
        e = self.elements
        self.assertTrue(self.login("spanish"))
        self.click(e.for_you_tab)
        self.assertTrue(self.urls.BLANK_HOME[0:35] in self.get_url(), "Unexpected URL")
        
    def test_prod_language_select_screen_load_non_core_language(self):
        e = self.elements
        self.assertTrue(self.login("korean"))
        self.click(e.for_you_tab)
        self.assertTrue(self.urls.BLANK_HOME[0:35] in self.get_url(), "Unexpected URL")
