from model.project import Project


def test_add_project(app, db):
    app.session.login(username="administrator", password="root")
    project = Project(name="New project3", description="Project description", status="development", view_state="public")
    old_projects_list = db.get_projects_list()
    app.project.create_project(project)
    app.session.logout()
    new_projects_list = db.get_projects_list()
    old_projects_list.append(project)
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)
