from selenium.webdriver.common.by import By

class LoginPage:
    # Locators
    txtbox_username_id = 'input-email'
    txt_password_id = 'input-password'
    button_login_xpath = "//input[@value='Login']"
    msg_myaccount_xpath = "//h2[text()='My Account']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"
    edit_your_account_information_option_link_text = "Edit your account information"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        usernametxt = self.driver.find_element(By.ID, self.txtbox_username_id)
        usernametxt.clear()
        usernametxt.send_keys(username)

    def setPassword(self, password):
        passwordtxt = self.driver.find_element(By.ID, self.txt_password_id)
        passwordtxt.clear()
        passwordtxt.send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
        except:
            return False

    def login_to_application(self, email_address_text, password_text):
        self.setUserName(email_address_text)
        self.setPassword(password_text)
        self.click_on_login_button()

    def retrieve_warning_message(self):
        try:
            return self.driver.find_element(By.XPATH, self.warning_message_xpath).text
        except:
            return None

    def display_status_of_edit_your_account_information_option(self):
        try:
            return self.driver.find_element(By.LINK_TEXT, self.edit_your_account_information_option_link_text).is_displayed()
        except:
            return False
