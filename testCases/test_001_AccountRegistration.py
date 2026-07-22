import email
import os.path
import random

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen # for logging


class Test_001_AccountRegistration:
    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_account_reg(self, setup):
        self.logger.info("***** Starting Test_001_AccountRegistration *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info(f"Opened application URL: {self.base_url}")

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.logger.info("Clicked on My Account link")
        self.hp.clickRegisterLink()
        self.logger.info("Clicked on Register link")

        self.regPage = AccountRegistrationPage(self.driver)
        self.regPage.setFirstName("Mahesh")
        self.logger.info("Entered First Name: Mahesh")
        self.regPage.setLastName("Patil")
        self.logger.info("Entered Last Name: Patil")

        self.email = randomeString.random_string_generator() + '@gmail.com'
        self.regPage.setEmail(self.email)
        self.logger.info(f"Entered Email: {self.email}")

        self.regPage.setTelephone("65656565")
        self.logger.info("Entered Telephone: 65656565")

        self.password = "admin@123"
        self.regPage.setPassword(self.password)
        self.regPage.setConfirmPassword(self.password)
        self.logger.info("Entered and confirmed Password")

        self.regPage.setPrivacyPolicy()
        self.logger.info("Accepted Privacy Policy")
        self.regPage.clickContinue()
        self.logger.info("Clicked Continue button")

        self.confmsg = self.regPage.getconfirmationmsg()
        self.logger.info(f"Confirmation message received: {self.confmsg}")

        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("Account registration successful")
            assert True

        else:
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, "test_account_reg.png")
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Account registration failed. Screenshot saved at {screenshot_path}")
            assert False



        self.logger.info("***** Finished Test_001_AccountRegistration *****")
