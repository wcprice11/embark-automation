import unittest
from sessions.embark_session import *
from sessions.embark_branch import web_prod, web_dev, web_rc, web_stage

class EmbarkTest(SessionMixIn, unittest.TestCase):
    def setUp(self) -> None: # runs before every test
        self.setUpVars()
        self.start()

    def setUpVars(self):
        pass

    def tearDown(self) -> None: # runs after every test
        self.save_screenshot(f"./report/{self.id()}.png")
        self.quit()

    # Helper test methods auto-generate error messages
    def validate_text(self, test:str, truth:str):
        self.assertEqual(test, truth, f"Unexpected text: '{test}'\n does not match '{truth}'")

    def validate_text_contains(self, test:str, truth:str):
        self.assertTrue(truth in test, f"Unexpected text: '{test}'\n does not contain '{truth}'")

    def validate_url(self, truth:str):
        self.assertEqual(self.get_url(), truth, f"Unexpected text: '{self.get_url()}'\n does not match '{truth}'")

    def validate_url_contains(self, truth:str):
        self.assertTrue(truth in self.get_url(), f"Unexpected text: '{self.get_url()}'\n does not contain '{truth}'")
    
    def validate_element_text(self, element, truth:str, contains=False):
        test = self.get_element(element).text
        if(contains): self.assertTrue(truth in test, f"Unexpected text: '{test}'\n does not contain '{truth}'")
        else: self.assertEqual(test, truth, f"Unexpected text: '{test}'\n does not match '{truth}'")

    def wait_for_text_in_element(self, element, text: str, time=30):
        return super()._wait_for_text_in_element(element[0:2], text, time)

    def find(self, element, time=30):
        self.assertTrue(self._find(element[0:2], time), f"couldn't find element {element[2]} by {element[0:2]}. This is likely a broken test")

    def click(self, element, time=30):
        self.assertTrue(self._click(element[0:2], time), f"couldn't find element {element[2]} by {element[0:2]}. This is likely a broken test")

    def fill(self, element, text:str, time=30, enter=False):
        self.assertTrue(self._fill(element[0:2], text, time, enter), f"couldn't find element {element[2]} by {element[0:2]}. This is likely a broken test")
    
    def get_element(self, element, time=30):
        self.find(element)
        return self._find(element[0:2])

    # MACRO FUNCTIONS
    def login(self, language=None):
        # either login via LDS account or API if available
        # FIX_ME
        e = self.elements
        self.get(self.urls.LOGIN)
        self.assertEqual(self.urls.LOGIN, self.get_url())
        self.click(e.sign_in_button)
        self.find(e.sign_in_username_field)
        self.fill(e.sign_in_username_field, self.user.username)
        self.click(e.sign_in_next)
        self.find(e.sign_in_password_field)
        self.fill(e.sign_in_password_field, self.user.get_password())
        self.click(e.sign_in_submit)
        self.wait_for_text_in_element(e.language_submit, "Submit")
        self.find(e.i_want_to_learn)
        self.assertEqual(self.get_url(), self.urls.ONBOARDING)
        if(language):
            self.fill(self.elements.i_want_to_learn, language, enter=True)
            self.click(self.elements.language_submit)
        return True


    def i_want_to_learn(self, language="spanish"):
        # self.click(self.elements.i_want_to_learn)
        self.fill(self.elements.i_want_to_learn, language, enter=True)
        self.click(self.elements.language_submit)
        # self.click(self.elements.whats_new_card_close_button) # This doesn't feel appropriate here
        # self.click(self.elements.home_button)
        # self.validate_url_contains(self.urls.BLANK_HOME)
        return True

class VisualEmbarkProdTest(BasicVisualProdSession, EmbarkTest):
    def setUpVars(self):
        self.load_branch(web_prod)

class EmbarkProdTest(EmbarkTest):
    def setUpVars(self):
        self.load_branch(web_prod)

class VisualEmbarkStageTest(BasicVisualStageSession, EmbarkTest):
    def setUpVars(self):
        self.load_branch(web_stage)

class EmbarkStageTest(EmbarkTest):
    def setUpVars(self):
        self.load_branch(web_stage)

class VisualEmbarkRCTest(BasicVisualRCSession, EmbarkTest):
    def setUpVars(self):
        self.load_branch(web_rc)

class EmbarkRCTest(EmbarkTest):
    def setUpVars(self):
        self.load_branch(web_rc)

class EmbarkDevTest(EmbarkTest):
    def setUpVars(self):
        self.load_branch(web_dev)
    