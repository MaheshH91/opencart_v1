from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.lnk_register_linktext = "Register"
        self.lnk_login_linktext = "Login"
        self.lnk_logout_linktext = "Logout"
        self.my_account_xpath = "//a[@title='My Account']"

    def clickRegisterLink(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_register_linktext).click()

    def clickLoginLink(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_login_linktext).click()

    def clickLogoutLink(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_logout_linktext).click()

    def clickMyAccount(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='My Account']"))
        ).click()
