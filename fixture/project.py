from selenium.webdriver.common.by import By
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_projects(self):
        browser = self.app.browser
        if not (browser.current_url.endswith("/manage_proj_page.php")
                and len(browser.find_elements(By.CSS_SELECTOR, "//input[@value='Create New Project']")) > 0):
            browser.find_element(By.LINK_TEXT, "Manage Projects").click()

    def create_project(self):
        browser = self.app.browser
        browser.get("http://localhost/mantisbt-1.2.20/manage_overview_page.php")
        browser.find_element_by_link_text("Manage").click()
        browser.find_element_by_link_text("Manage Projects").click()
        browser.find_element_by_xpath("//input[@value='Create New Project']").click()
        browser.find_element_by_name("name").click()
        browser.find_element_by_name("name").clear()
        browser.find_element_by_name("name").send_keys("sadsdad")
        browser.find_element_by_name("status").click()
        browser.find_element_by_name("status").click()
        browser.find_element_by_name("view_state").click()
        browser.find_element_by_name("view_state").click()
        browser.find_element_by_name("description").click()
        browser.find_element_by_name("description").clear()
        browser.find_element_by_name("description").send_keys("asfsdfsdfg")
        browser.find_element_by_xpath("//input[@value='Add Project']").click()