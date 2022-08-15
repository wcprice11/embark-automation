from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Driver(webdriver.Chrome):
    def __init__(self):
        driver_path = ".\\drivers"
        self.service = ChromeService(ChromeDriverManager(path=driver_path).install())
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])

    def launch(self):
        super().__init__(service=self.service, options=self.options)

basicDriver = Driver()