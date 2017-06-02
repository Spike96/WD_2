from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.manage_location import ManageLocationHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.manage_location = ManageLocationHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://wd2.fintegro.ca/login")

    def destroy(self):
        self.wd.quit()