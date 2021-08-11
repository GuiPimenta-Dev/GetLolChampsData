from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

# DRIVER_PATH = "driver\chromedriver.exe"

class BasePage(object):
    
    url = None

    def __init__(self):
        options = self._get_driver_options()
        self.driver = webdriver.Chrome(chrome_options=options)

    def go(self):
        self.driver.get(self.url)

    def _get_driver_options(self):
        options = Options()
        options.add_argument('--no-sandbox')
        options.Proxy = None
        options.add_argument('--disable-gpu')
        options.add_argument('log-level=3')
        options.add_argument('--headless')
        options.add_argument("--disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })
        return options

    def close(self):
        self.driver.close()
        self.driver.quit()

    def get_soup(self) -> BeautifulSoup:
        return BeautifulSoup(self.driver.page_source, 'lxml')