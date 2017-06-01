from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(15)
        self.session = SessionHelper(self)

    def destroy(self):
        self.wd.quit()