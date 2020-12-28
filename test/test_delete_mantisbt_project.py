from model.project import Project
import random


def test_delete_project(app, db):
    app.session.login(username="administrator", password="root")
    if len(db.get_projects_list()) == 0:
        app.project.create(
            Project(name="New project", description="Project description", status="development", view_state="public"))
    old_projects_list = db.get_projects_list()
    project_for_delete = random.choice(old_projects_list)
    app.project.delete_project_by_name(project_for_delete.name)
    app.session.logout()
    new_projects_list = db.get_projects_list()
    old_projects_list.remove(project_for_delete)
    assert old_projects_list == new_projects_list
