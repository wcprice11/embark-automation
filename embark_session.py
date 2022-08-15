from embark_user import *
from embark_branch import *
from driver import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Session():
    def __init__(self, user=blank_user, branch=WebProd, driver=basicDriver) -> None:
        self.user = user
        self.branch = branch
        self.driver = driver

    # webDriver control
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

    
    # User control
    def load_user(self, user: User):
        self.user = user

    def reset_user(self) -> None:
        self.user.reset()
    

    # Branch Control
    # this might not be needed
    def load_branch(self, branch: Branch):
        self.branch = branch
        self.driver.close()
        self.driver.launch()
    
    # Basic Navigation
    def find(self, element, time=100):
        try:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(element)
            )
        except:
            return None
        return self.driver.find_element(*element)
        
    def click(self, element, time=100):
        try:
            WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable(element)
            )
            self.driver.find_element(*element).click()
        except:
            return None
        return True

    def fill(self, element, text: str, time=100):
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
    # macros-these would have to be completely general
    """    
    def login(self):
        # either login via LDS account or API if available
        # FIX_ME
        pass

    def logout(self):
        self.click(E.settings)
        self.click(E.logout)
        pass"""


    

webProdSession = Session()

    # login_page = pages.prod_login
"""    
class webStageSession(Session):
    def __init__(self, user=basic_user, branch=WebStage, driver=basicDriver) -> None:
        super().__init__(self, user, branch, driver)

class webRCSession(Session):
    def __init__(self, user=basic_user, branch=WebRC, driver=basicDriver) -> None:
        super().__init__(self, user, branch, driver)

class webDevSession(Session):
    def __init__(self, user=basic_user, branch=WebDev, driver=basicDriver) -> None:
        super().__init__(self, user, branch, driver)
        """
