import pytest

from src.app.application import Application


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    return Application(url)


@pytest.fixture(scope="class")
def disk_api(app):
    return app.disk_api


@pytest.fixture(scope="class")
def auth(request):
    request.cls.auth = {'Authorization': 'y0_AgAAAABqM4PDAAnOqQAAAADhuCtW-neeWjrGT0yMkBb3sHTppvj6Faw'}


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api host",
        default="https://cloud-api.yandex.net",
    ),
