from sessions.embark_user import *
from sessions.driver import *
from sessions.embark_branch import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Session():
    def __init__(self, user=test_user_00, branch=web_prod, driver=Driver()) -> None:
        self.user = user
        self.branch = branch
        self.driver = driver
        self.elements = self.branch.elements
        self.URLs = self.branch.urls

    # WebDriver control

    # starts the webdriver
    def start(self):
        self.driver.launch()
    # navigates to a url
    def get(self, url:str):
        self.driver.get(url)
        pass
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

    # this might not be needed
    def load_branch(self, branch):
        self.branch = branch
        self.driver.close()
        self.driver.launch()
    

    # Basic Navigation

    def find(self, element, time=30):
        try:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(element)
            )
        except:
            return None
        return self.driver.find_element(*element)
        
    def click(self, element, time=30):
        try:
            WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable(element)
            )
            self.driver.find_element(*element).click()
        except:
            return None
        return True

    def fill(self, element, text: str, time=30):
        try:
            WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable(element)
            )
            self.driver.find_element(*element).send_keys(text)
        except:
            return None
        return self.driver.find_element(*element)

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
