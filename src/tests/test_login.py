import unittest
from sessions.embark_session import Session
from sessions.embark_branch import web_prod, web_dev, web_rc, web_stage

class TestProdLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.session = Session()
        self.session.start()

    def test_login_page(self):
        s = self.session
        u = s.URLs
        e = s.elements
        s.get(s.URLs.LOGIN)
        self.assertEqual(u.LOGIN, s.get_url(), "Unexpected URL")
        s.click(e.sign_in_button)
        s.find(e.sign_in_username_field)
        s.fill(e.sign_in_username_field, s.user.username)
        s.click(e.sign_in_next)
        s.find(e.sign_in_password_field)
        s.fill(e.sign_in_password_field, s.user.get_password())
        s.click(e.sign_in_submit)
        s.find(e.i_want_to_learn)
        self.assertEqual(s.get_url(), u.ONBOARDING, "Unexpected URL")

    
    def test_macro_login(self):
        self.assertTrue(self.session.login(), "login macro failed")
        self.assertTrue(self.session.URLs.BLANK_HOME in self.session.get_url(), "Unexpected URL")

    def tearDown(self) -> None:
        self.session.save_screenshot(f"./report/{self.id()}.png")
        self.session.quit()

class TestStageLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.session = Session(branch=web_stage)
        self.session.start()
    
    def test_macro_login(self):
        self.assertTrue(self.session.login(), "login macro failed")
        self.assertEqual(self.session.get_url(), self.session.URLs.BLANK_HOME, "Unexpected URL")

    def tearDown(self) -> None:
        self.session.save_screenshot(f"./report/{self.id()}.png")
        self.session.quit()

class TestRCLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.session = Session(branch=web_rc)
        self.session.start()
    
    def test_macro_login(self):
        self.assertTrue(self.session.login(), "login macro failed")
        self.assertEqual(self.session.get_url(), self.session.URLs.BLANK_HOME, "Unexpected URL")

    def tearDown(self) -> None:
        self.session.save_screenshot(f"./report/{self.id()}.png")
        self.session.quit()

class TestDevLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.session = Session(branch=web_dev)
        self.session.start()
    
    def test_macro_login(self):
        self.assertTrue(self.session.login(), "login macro failed")
        self.assertEqual(self.session.get_url(), self.session.URLs.BLANK_HOME, "Unexpected URL")

    def tearDown(self) -> None:
        self.session.save_screenshot(f"./report/{self.id()}.png")
        self.session.quit()