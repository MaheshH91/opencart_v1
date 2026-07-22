import os
import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_Login:
    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("******* Starting test_002_login *******")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info(f"Opened application URL: {self.base_url}")

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.logger.info("Clicked on My Account link")
        self.hp.clickLoginLink()
        self.logger.info("Clicked on Login link")

        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName("holkarmahesh1@gmail.com")
        self.loginPage.setPassword("admin@123")
        self.loginPage.click_on_login_button()
        self.logger.info("Entered credentials and clicked Login")

        time.sleep(2)
        act_title = self.driver.title
        self.logger.info(f"Page title after login: {act_title}")

        if act_title == "My Account":
            self.logger.info("Login test passed")
            assert True
        else:
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, "test_login.png")
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Login test failed. Screenshot saved at {screenshot_path}")
            assert False


        self.logger.info("******* Finished test_002_login *******")
