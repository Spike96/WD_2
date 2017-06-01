# -*- coding: utf-8 -*-

import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login_logout(app):
    app.open_home_page()
    app.login(username="QACam", password="QACam12")
    app.select_company()
    app.logout()
