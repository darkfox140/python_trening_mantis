from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.james import JamesHelper
from fixture.soap import SoapHelper


class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.browser = webdriver.Firefox()
        elif browser == "chrome":
            self.browser = webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.browser.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.mail = MailHelper(self)
        self.signup = SignupHelper(self)
        self.soap = SoapHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']

    def is_valid(self):
        try:
            self.browser.current_url
            return True
        except:
            return False

    def open_home_page(self):
        browser = self.browser
        browser.get(self.base_url)

    def destroy(self):
        self.browser.quit()
