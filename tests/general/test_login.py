from tests.embark_test_classes import *

class TestProdLogin(EmbarkProdTest):
    def test_login_page(self):
        u = self.urls
        e = self.elements
        self.get(u.LOGIN)
        self.validate_url_contains(u.LOGIN)
        self.click(e.sign_in_button)
        self.find(e.sign_in_username_field)
        self.fill(e.sign_in_username_field, self.user.username)
        self.click(e.sign_in_next)
        self.find(e.sign_in_password_field)
        self.fill(e.sign_in_password_field, self.user.get_password())
        self.click(e.sign_in_submit)
        self.find(e.i_want_to_learn)
        self.validate_url(u.ONBOARDING)

    
    def test_macro_login(self):
        self.assertTrue(self.login(), "login macro failed")
        self.validate_url_contains(self.urls.ONBOARDING)


class TestRCLogin(EmbarkRCTest):
    def test_macro_login(self):
        self.assertTrue(self.login(), "login macro failed")
        self.validate_url_contains(self.urls.ONBOARDING)

