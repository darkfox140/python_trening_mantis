from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        browser = self.app.browser
        if not (browser.current_url.endswith("manage_proj_page.php")):
            browser.find_element_by_link_text("Manage").click()
            browser.find_element_by_link_text("Manage Projects").click()

    def change_field_value(self, field_name, text):
        browser = self.app.browser
        if text is not None:
            browser.find_element(By.NAME, field_name).click()
            browser.find_element(By.NAME, field_name).clear()
            browser.find_element(By.NAME, field_name).send_keys(text)

    def change_option_value(self, field_name, option):
        browser = self.app.browser
        if option is not None:
            browser.find_element_by_name(field_name).click()
            Select(browser.find_element_by_name(field_name)).select_by_visible_text(option)

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_option_value("status", project.status)
        self.change_option_value("view_state", project.view_state)
        self.change_field_value("description", project.description)

    def get_projects_list(self):
        browser = self.app.browser
        self.open_project_page()
        project_table = browser.find_elements(By.TAG_NAME, "table")[2]
        project_rows = project_table.find_elements(By.TAG_NAME, "tr")[2:]
        project_list = []
        for element in project_rows:
            cells = element.find_elements(By.TAG_NAME, "td")
            id = cells[0].find_element(By.TAG_NAME, "a").get_attribute("href")
            id.replace("http://localhost/mantis/manage_proj_edit_page.php?project_id=", "")
            name = cells[0].find_element(By.TAG_NAME, "a").text
            status = cells[1].text
            view_state = cells[3].text
            description = cells[4].text
            project_list.append\
                (Project(id=id, name=name, status=status, view_state=view_state, description=description))
        return project_list

    def create_project(self, project):
        browser = self.app.browser
        self.open_project_page()
        browser.find_element_by_xpath("//input[@type='submit' and @value='Create New Project']").click()
        self.fill_project_form(project)
        browser.find_element_by_xpath("//input[@value='Add Project']").click()
