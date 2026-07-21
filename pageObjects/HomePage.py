from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.lnk_register_linktext = "Register"

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()

    def clickRegisterLink(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_register_linktext).click()
