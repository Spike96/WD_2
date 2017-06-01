from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(15)

    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath("//nav/div[4]/a").click()
        wd.find_element_by_link_text("Logout").click()

    def select_company(self):
        wd = self.wd
        if not wd.find_element_by_xpath("//select[@id='companies']//option[2]").is_selected():
            wd.find_element_by_xpath("//select[@id='companies']//option[2]").click()
        wd.find_element_by_id("select").click()

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_css_selector("a.a_login.btn_submit").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://wd2.fintegro.ca/login")

    def destroy(self):
        self.wd.quit()