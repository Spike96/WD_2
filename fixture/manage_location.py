
class ManageLocationHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_location(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='tile-container']/div[3]/div[1]").click()

    def add_location(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@id='btn-add-location']//span[.='Add Location']").click()
        wd.find_element_by_id("OpenLayers.Geometry.Point_243").click()
        wd.find_element_by_link_text("OK").click()

    def fill_data(self):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//select[@id='timezone_id']//option[324]").is_selected():
            wd.find_element_by_xpath("//select[@id='timezone_id']//option[324]").click()
        wd.find_element_by_id("name").click()
        wd.find_element_by_id("name").clear()
        wd.find_element_by_id("name").send_keys("Magenta, Montataire")
        wd.find_element_by_link_text("OK").click()