# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login_logout(app):
    app.session.open_home_page()
    app.session.login(username="QACam", password="QACam12")
    app.session.select_company()
    app.session.logout()
 