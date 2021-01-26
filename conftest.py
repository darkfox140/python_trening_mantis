import pytest
import os.path
from fixture.application import Application
import json
from fixture.db import DbFixture
from fixture.orm import ORMFixture
import ftputil

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    # webadmin_config = load_config(request.config.getoption("--target"))['webadmin']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=config['web']['baseUrl'])
    # fixture.session.ensure_login(username=webadmin_config['username'], password=webadmin_config['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                          password=db_config['password'], )

    def fin():
        dbfixture.destroy()

    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session")
def orm(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    ormfixture = ORMFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                            password=db_config['password'])

    return ormfixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
