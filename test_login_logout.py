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
        self.wd.implicitly_wait(60)
    
    def test_test_login_logout(self):
        success = True
        wd = self.wd
        wd.get("http://wd2.fintegro.ca/login")
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys("QACam")
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("QACam12")
        wd.find_element_by_css_selector("a.a_login.btn_submit").click()
        if not wd.find_element_by_xpath("//select[@id='companies']//option[2]").is_selected():
            wd.find_element_by_xpath("//select[@id='companies']//option[2]").click()
        wd.find_element_by_id("select").click()
        wd.find_element_by_link_text("Logout").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
