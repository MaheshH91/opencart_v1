from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.lnk_register_linktext = "Register"
        self.lnk_login_linktext = "Login"
        self.lnk_logout_linktext = "Logout"
        self.my_account_xpath = "//span[text()='My Account']"

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def clickRegisterLink(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_register_linktext).click()

    def clickLoginLink(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_login_linktext).click()

    def clickLogoutLink(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_logout_linktext).click()
    
