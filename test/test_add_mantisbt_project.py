

def test_untitled_test_case(app):
    app.session.login("administrator", "root")
    app.project.create_project()
