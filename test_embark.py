import unittest
import embark_session
import URLs
import element as E
import embark_user



class TestEmbark(unittest.TestCase):
    def setUp(self) -> None:
        self.session = embark_session.webProdSession
        self.session.load_user(embark_user.test_user_00)
        self.session.start()

    
    def test_login_page_prod(self):
        s = self.session
        s.get(URLs.PROD_LOGIN)
        self.assertEqual(URLs.PROD_LOGIN, s.get_url())
        s.click(E.sign_in_button)
        s.find(E.sign_in_username_field)
        s.fill(E.sign_in_username_field, s.user.username)
        s.click(E.sign_in_next)
        s.find(E.sign_in_password_field)
        s.fill(E.sign_in_password_field, s.user.get_password())
        s.click(E.sign_in_submit)
        s.find(E.i_want_to_learn)
        self.assertEqual(s.get_url(), URLs.PROD_ONBOARDING)
        s.click(E.i_want_to_learn)
        s.click(E.french)
        s.click(E.language_submit)
        s.click(E.for_you_tab)
        self.assertEqual(s.get_url(), URLs.PROD_HOME_PAGE)

    def test_login_page_stage(self):
        s = self.session
        s.get(URLs.STAGE_LOGIN)
        self.assertEqual(URLs.STAGE_LOGIN, s.get_url())
        s.click(E.sign_in_button)
        s.find(E.sign_in_username_field)
        s.fill(E.sign_in_username_field, s.user.username)
        s.click(E.sign_in_next)
        s.find(E.sign_in_password_field)
        s.fill(E.sign_in_password_field, s.user.get_password())
        s.click(E.sign_in_submit)
        s.find(E.i_want_to_learn)
        self.assertEqual(s.get_url(), URLs.STAGE_ONBOARDING)
        s.click(E.i_want_to_learn)
        s.click(E.french)
        s.click(E.language_submit)
        s.click(E.for_you_tab)
        self.assertEqual(s.get_url(), URLs.STAGE_HOME_PAGE)

    def test_login_page_rc(self):
        s = self.session
        s.get(URLs.RC_LOGIN)
        self.assertEqual(URLs.RC_LOGIN, s.get_url())
        s.click(E.sign_in_button)
        s.find(E.sign_in_username_field)
        s.fill(E.sign_in_username_field, s.user.username)
        s.click(E.sign_in_next)
        s.find(E.sign_in_password_field)
        s.fill(E.sign_in_password_field, s.user.get_password())
        s.click(E.sign_in_submit)
        s.find(E.i_want_to_learn)
        self.assertEqual(s.get_url(), URLs.RC_ONBOARDING)
        s.click(E.i_want_to_learn)
        s.click(E.french)
        s.click(E.language_submit)
        s.click(E.for_you_tab)
        self.assertEqual(s.get_url(), URLs.RC_HOME_PAGE)
        
    def test_login_page_dev(self):
        s = self.session
        s.get(URLs.DEV_LOGIN)
        self.assertEqual(URLs.DEV_LOGIN, s.get_url())
        s.click(E.sign_in_button)
        s.find(E.sign_in_username_field)
        s.fill(E.sign_in_username_field, s.user.username)
        s.click(E.sign_in_next)
        s.find(E.sign_in_password_field)
        s.fill(E.sign_in_password_field, s.user.get_password())
        s.click(E.sign_in_submit)
        s.find(E.i_want_to_learn)
        self.assertEqual(s.get_url(), URLs.DEV_ONBOARDING)
        s.click(E.i_want_to_learn)
        s.click(E.french)
        s.click(E.language_submit)
        s.click(E.for_you_tab)
        s.find(E.home_button)
        self.assertEqual(s.get_url(), URLs.DEV_HOME_PAGE)


    def tearDown(self) -> None:
        self.session.quit()

if __name__ == "__main__":
    unittest.main()