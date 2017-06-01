# -*- coding: utf-8 -*-


def test_login_logout(app):
    app.open_home_page()
    app.session.login(username="QACam", password="QACam12")
    app.session.select_company()
    app.session.logout()
