from model.project import Project


def test_add_project(app, db):
    project = Project(name="New project", description="Project description", status="development", view_state="public")
    old_projects_list = db.get_projects_list()
    app.session.login(username="administrator", password="root")
    app.project.create_project(project)
    app.session.logout()
    new_projects_list = db.get_projects_list()
    old_projects_list.append(project)
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)
