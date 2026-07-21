import email
import os.path
import random
from utilities.randomeString import random_string_generator
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString


class Test_001_AccountRegistration:
    base_url = "https://tutorialsninja.com/demo/"

    def test_account_reg(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegisterLink()
        self.regPage = AccountRegistrationPage(self.driver)
        self.regPage.setFirstName("Mahesh")
        self.regPage.setLastName("Patil")
        self.email = randomeString.random_string_generator() + '@gmail.com'
        self.regPage.setEmail(self.email)
        self.regPage.setTelephone("65656565")
        self.password= "admin@123"
        self.regPage.setPassword(self.password)
        self.regPage.setConfirmPassword(self.password)
        self.regPage.setPrivacyPolicy()
        self.regPage.clickContinue()
        self.confmsg = self.regPage.getconfirmationmsg()


        if self.confmsg == "Your Account Has Been Creat!":
            assert True
        else:
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            self.driver.save_screenshot(
                os.path.join(screenshot_dir, "test_account_reg.png")
            )
            assert False

        self.driver.close()




