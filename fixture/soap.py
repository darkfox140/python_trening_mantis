from model.project import Project
from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        l = client.service.mc_projects_get_user_accessible(username, password)
        project_list = []
        for el in l:
            id = el[0]
            name = el[1]
            description = el[7]
            project_list.append(Project(id=str(id), name=name, description=description))
        return project_list
