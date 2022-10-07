import unittest
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
        s.click(e.learn_spanish)
        s.click(e.language_submit)
        s.click(e.for_you_tab)
        self.assertTrue(u.BLANK_HOME[0:35] in s.get_url(), "Unexpected URL")
        s.click(e.settings_button)
        self.assertEqual(u.SETTINGS, s.get_url, "Unexpected URL")
        s.click(e.contact_us_button)
        self.assertEqual(u.CONTACT_US, s.get_url, "Unexpected URL")
        s.click(e.settings_button)
        self.assertEqual(u.SETTINGS, s.get_url, "Unexpected URL")
        s.click(e.troubleshooting_button)
        self.assertEqual(u.TROUBLE_SHOOTING, s.get_url, "Unexpected URL")
        s.click(e.settings_button)
        self.assertEqual(u.SETTINGS, s.get_url, "Unexpected URL")
        s.click(e.about_button)
        self.assertEqual(u.ABOUT, s.get_url, "Unexpected URL")
        

        
        
 


        
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
