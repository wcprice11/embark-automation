import unittest
from sessions.embark_session import *
from sessions.embark_branch import web_prod, web_dev, web_rc, web_stage
from time import sleep
# from pytest_html_reporter import attach

class EmbarkTest(SessionMixIn, unittest.TestCase):
    def setUp(self) -> None: # runs before every test
        self.setUpVars()
        self.start()

    def setUpVars(self):
        pass

    def tearDown(self) -> None: # runs after every test
        # attach(data=self.driver.get_screenshot_as_png())
        self.quit()

    # Helper test methods auto-generate error messages
    def validate_text(self, test:str, truth:str):
        self.assertEqual(test, truth, f"Unexpected text: '{test}'\n does not match '{truth}'")

    def validate_text_contains(self, test:str, truth:str):
        self.assertTrue(truth in test, f"Unexpected text: '{test}'\n does not contain '{truth}'")

    def validate_text_absent(self, test:str, truth:str):
        self.assertFalse(truth in test, f"Unexpected text: '{test}'\n should not contain '{truth}'")

    def validate_url(self, truth:str):
        self.assertEqual(self.get_url(), truth, f"Unexpected text: '{self.get_url()}'\n does not match '{truth}'")

    def validate_url_contains(self, truth:str):
        self.assertTrue(truth in self.get_url(), f"Unexpected text: '{self.get_url()}'\n does not contain '{truth}'")
    
    def validate_element_text(self, element, truth:str, contains=False):
        test = self.get_element(element).text
        if(contains): self.assertTrue(truth in test, f"Unexpected text: '{test}'\n does not contain '{truth}'")
        else: self.assertEqual(test, truth, f"Unexpected text: '{test}'\n does not match '{truth}'")
    
    # Waits
    def wait_for_text_in_element(self, element, text: str, time=30):
        self.assertTrue(super()._wait_for_text_in_element(element[0:2], text, time), f"Took too long to find {element[2]} with text {text}")
    
    def wait_for_element_to_be_clickable(self, element, time=30):
        self.assertTrue(super()._wait_for_element_to_be_clickable(element[0:2], time), f"Took too long for {element[2]} to be clickable")

    def wait_for_text_in_url(self, text:str, time=30):
        self.assertTrue(super()._wait_for_text_in_url(text, time), f"Took too long to find {text} in url. current url: {self.get_url()}")

    # page navigation and interaction
    def find(self, element, time=30):
        self.assertTrue(self._find(element[0:2], time), f"couldn't find element {element[2]} by {element[0:2]}. This is likely an out of date CSS Selector")

    def click(self, element, time=30):
        self.assertTrue(self._click(element[0:2], time), f"couldn't find element {element[2]} by {element[0:2]}. This is likely an out of date CSS Selector")

    def fill(self, element, text:str, time=30, enter=False):
        self.assertTrue(self._fill(element[0:2], text, time, enter), f"couldn't find element {element[2]} by {element[0:2]}. This is likely an out of date CSS Selector")
    
    def get_element(self, element, time=30):
        self.find(element)
        return self._find(element[0:2])

    def reload(self):
        return super()._reload()

    # MACRO FUNCTIONS
    def login(self, language=None, attempts=0):
        # either login via LDS account or API if available
        # FIX_ME
        e = self.elements
        self.get(self.urls.LOGIN)
        self.assertEqual(self.urls.LOGIN, self.get_url())
        self.click(e.sign_in_button)
        self.find(e.sign_in_username_field)
        self.fill(e.sign_in_username_field, self.user.username)
        self.click(e.sign_in_next)
        elems = self.driver.find_elements(*self.elements.too_many_attempts_message[0:2])
        if (self.driver.find_elements(*self.elements.too_many_attempts_message[0:2])): 
            if (attempts > 4):
                self.fail("Too many login attempts")
            sleep(100)
            return self.login(language=language, attempts=attempts + 1)
        self.find(e.sign_in_password_field)
        self.fill(e.sign_in_password_field, self.user.get_password())
        self.click(e.sign_in_submit)
        if (   # Clause to catch 503 errors when the app is updating.
            self.driver.find_elements(*self.elements.error_message[0:2]) and 
            "503" in self.driver.find_element(*self.elements.error_message[0:2]).text
        ): 
            sleep(5)
            self.reload()
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
    