from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



class Driver(webdriver.Chrome):
    def __init__(self, headless = True):
        driver_path = ".\\drivers"
        self.service = ChromeService(ChromeDriverManager(os_type="mac_arm64", path=driver_path).install())
        
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        if(headless):
            self.options.add_argument('headless')
        self.launched = False

    def launch(self):
        self.launched = True
        super().__init__(service=self.service, options=self.options)

