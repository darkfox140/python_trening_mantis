import re
from selenium.webdriver.common.by import By


class SignupHelper:

    def __init__(self, app):
        self.app = app

    def new_user(self, email, username, password):
        browser = self.app.browser
        browser.get(self.app.base_url + "/signup_page.php")
        browser.find_element(By.NAME, "username").send_keys(username)
        browser.find_element(By.NAME, "email").send_keys(email)
        browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        url = self.extract_confirmation_url(mail)

        browser.get(url)
        browser.find_element(By.NAME, "password").send_keys(password)
        browser.find_element(By.NAME, "password_confirm").send_keys(password)
        browser.find_element(By.CSS_SELECTOR, 'input[value="Update User"]').click()

    def extract_confirmation_url(self, text):
        return re.search("http://.*$", text, re.MULTILINE).group(0)
