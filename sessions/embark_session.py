
from sessions.embark_user import *
from sessions.driver import *
from sessions.embark_branch import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# This is being implemented as a mix-in so be careful with namespace errors
class SessionMixIn:
    def __init__(self, methodName:str, user=test_user_00, branch=web_stage, driver=Driver()) -> None:
        self.user = user
        self.branch = branch
        self.driver = driver
        self.elements = self.branch.elements
        self.urls = self.branch.urls
        super().__init__(methodName=methodName)

    # WebDriver control

    # starts the webdriver
    def start(self):
        self.driver.launch()
        self.driver.set_window_size(1366, 768)
    # navigates to a url
    def get(self, url:str, tries=0):
        self.driver.get(url)
        if (   # Clause to catch 503 errors when the app is updating.
            self.driver.find_elements(*self.elements.error_message[0:2]) and 
            "503" in self.driver.find_element(*self.elements.error_message[0:2]).text and 
            tries < 5
        ): 
            sleep(5)
            return self.get(url, tries + 1)
        if (tries >= 5):
            raise Exception("Server error is preventing page load")
    # closes webdriver
    def quit(self):
        self.driver.close()
    # saves a screenshot to the listed directory. Must be a png filename.
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename=filename)

    
    # User control

    def load_user(self, user: User):
        self.user = user

    def reset_user(self) -> None:
        self.user.reset()
    

    # Branch Control

    def load_branch(self, branch):
        self.branch = branch


    # Driver Control

    def load_driver(self, driver: Driver):
        if(self.driver.launched and self.driver.session_id):
            self.driver.close()
        self.driver = driver
        self.start()
    

    # Basic Navigation

    def _find(self, element, time=30):
        try:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(element)
            )
            elem = self.driver.find_element(*element)
            if(not elem.is_displayed()):
                WebDriverWait(self.driver, time).until(
                    EC.presence_of_element_located(element)
                )
                ActionChains(self.driver).move_to_element(elem).perform()
        except TimeoutException:
            return None
        return elem
        
    def _click(self, element, time=30):
        try:
            self._find(element, time)
            WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable(element)
            )
            self.driver.find_element(*element).click()
        except TimeoutException:
            return None
        return True

    def _fill(self, element, text: str, time=30, enter=False):
        try:
            self._find(element, time)
            WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable(element)
            )
            self.driver.find_element(*element).send_keys(text)
            if (enter):
                self.driver.find_element(*element).send_keys(Keys.ENTER)
        except TimeoutException:
            return None
        return self.driver.find_element(*element)

    def _wait_for_text_in_element(self, element, text: str, time=30):
        try: 
            WebDriverWait(self.driver, time).until(
                EC.text_to_be_present_in_element(element, text)
            )
        except TimeoutException:
            return False
        return True

    def _wait_for_element_to_be_clickable(self, element, time=30):
        try: 
            WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable(element)
            )
        except TimeoutException:
            return False
        return True

        
    def get_url(self) -> str:
        return self.driver.current_url
    
    def get_title(self) -> str:
        return self.driver.title


    # macros
    # these have to be completely general
    def login(self):
        # either login via LDS account or API if available
        # FIX_ME
        u = self.URLs
        e = self.elements
        self.get(self.URLs.LOGIN)
        if (u.LOGIN==self.get_url()):
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

    def logout(self):
        self.click(self.session.elements.settings)
        self.click(self.session.elements.logout)
        pass

class BasicVisualProdSession:
    def __init__(self, methodName:str) -> None:
        super().__init__(methodName=methodName, user=test_user_00, branch=web_prod, driver=Driver(False))

class BasicVisualStageSession:
    def __init__(self, methodName:str) -> None:
        super().__init__(methodName=methodName, user=test_user_00, branch=web_stage, driver=Driver(False))

class BasicVisualRCSession:
    def __init__(self, methodName:str) -> None:
        super().__init__(methodName=methodName, user=test_user_00, branch=web_rc, driver=Driver(False))

class BasicVisualDevSession:
    def __init__(self, methodName:str) -> None:
        super().__init__(methodName=methodName, user=test_user_00, branch=web_dev, driver=Driver(False))
