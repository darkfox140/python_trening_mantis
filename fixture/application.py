from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.browser = webdriver.Firefox()
        elif browser == "chrome":
            self.browser = webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.browser.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.base_url = base_url

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
