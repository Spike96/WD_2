# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_login_logout(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(15)
    
    def test_login_logout(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="QACam", password="QACam12")
        self.select_company(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_xpath("//nav/div[4]/a").click()
        wd.find_element_by_link_text("Logout").click()

    def select_company(self, wd):
        if not wd.find_element_by_xpath("//select[@id='companies']//option[2]").is_selected():
            wd.find_element_by_xpath("//select[@id='companies']//option[2]").click()
        wd.find_element_by_id("select").click()

    def login(self, wd, username, password):
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_css_selector("a.a_login.btn_submit").click()

    def open_home_page(self, wd):
        wd.get("http://wd2.fintegro.ca/login")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
