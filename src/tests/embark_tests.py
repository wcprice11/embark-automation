import unittest
from sessions.embark_session import Session
from sessions.embark_branch import web_prod, web_dev, web_rc, web_stage

class EmbarkTest(unittest.TestCase):
    # 
    def setUp(self) -> None: # runs before every test
        self.setUpVars()
        self.session.driver.launch()
    
    # __init__() might be better but it requires getting into the guts of unittest.
    # might do that later, but for now, this works.
    def setUpVars(self):    
        self.urls = self.session.URLs
        self.elements = self.session.elements
    
    def tearDown(self) -> None: # runs after every test
        self.session.save_screenshot(f"./report/{self.id()}.png")
        self.session.quit()


    # Driver methods
    def get(self, url:str):
        self.session.driver.get(url)

    def quit(self):
        self.session.driver.close()

    def save_screenshot(self, filename): # filename must be a .png
        self.session.driver.save_screenshot(filename=filename)
    # FIX ME
    def save_element_screenshot(self, element, filename):
        pass
    
    # Pass-through methods to session for cleaner tests
    def find(self, element, time=30): # returns the element if present and None if not found in time
        return self.session.find(element, time)
    
    def click(self, element, time=30): # True if successful None if not found in time
        return self.session.click(element, time)

    def fill(self, element, text: str, time=30):
        self.session.fill(element, text, time)
    
    def get_url(self) -> str:
        return self.session.get_url()
    
    def get_title(self) -> str:
        return self.session.get_title()

    # Helper test methods auto-generate error messages
    def validate_text(self, test:str, truth:str):
        self.assertEqual(test, truth, f"Unexpected text: '{test}'\n does not match '{truth}'")

    def validate_text_contains(self, test:str, truth:str):
        self.assertTrue(truth in test, f"Unexpected text: '{test}'\n does not contain '{truth}'")

    def validate_url(self, truth:str):
        self.assertEqual(self.session.get_url(), truth, f"Unexpected text: '{self.session.get_url()}'\n does not match '{truth}'")

    def validate_url_contains(self, truth:str):
        self.assertTrue(truth in self.session.get_url(), f"Unexpected text: '{self.session.get_url()}'\n does not contain '{truth}'")

    # MACRO FUNCTIONS
    def login(self):
        # either login via LDS account or API if available
        # FIX_ME
        u = self.session.URLs
        e = self.session.elements
        self.get(self.URLs.LOGIN)
        if (u.LOGIN==self.get_url()):
            self.validate_text(e.sign_in_button, "Sign in")
            self.click(e.sign_in_button)
            self.find(e.sign_in_username_field)
            self.fill(e.sign_in_username_field, self.user.username)
            self.click(e.sign_in_next)
            self.find(e.sign_in_password_field)
            self.fill(e.sign_in_password_field, self.user.get_password())
            self.click(e.sign_in_submit)
            self.find(e.i_want_to_learn)
            if (self.get_url()==u.ONBOARDING): return True
        return False



class EmbarkProdTest(EmbarkTest):
    def setUpVars(self):
        self.session = Session(branch=web_prod)
        self.urls = self.session.URLs
        self.elements = self.session.elements

class EmbarkStageTest(EmbarkTest):
    def setUpVars(self):
        self.session = Session(branch=web_stage)
        self.urls = self.session.URLs
        self.elements = self.session.elements

class EmbarkRCTest(EmbarkTest):
    def setUpVars(self):
        self.session = Session(branch=web_rc)
        self.urls = self.session.URLs
        self.elements = self.session.elements

class EmbarkDevTest(EmbarkTest):
    def setUpVars(self):
        self.session = Session(branch=web_dev)
        self.urls = self.session.URLs
        self.elements = self.session.elements
    