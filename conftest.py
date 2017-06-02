import pytest
from fixture.application import Application


@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    fixture.open_home_page()
    # the bottom string be able to be uncommented and removed from tests
    # fixture.session.login(username="QACam", password="QACam12")
    # fixture.session.select_company()
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture