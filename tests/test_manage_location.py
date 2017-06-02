


def test_manage_location(app):
    app.open_home_page()
    app.session.login(username="QACam", password="QACam12")
    app.session.select_company()
    app.manage_location.open_manage_location()
    app.manage_location.add_location()
    app.manage_location.fill_data()
    app.session.logout()
