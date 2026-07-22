from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyAccountPage:
    # Locators
    # Standard OpenCart sidebar/dropdown logout link fallback locator
    _LNK_LOGOUT_XPATH = "//a[text()='Logout'] | //ul//a[text()='Logout']"

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def click_logout_button(self) -> None:
        """Waits for the logout link to be clickable and performs click."""
        logout_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self._LNK_LOGOUT_XPATH))
        )
        logout_element.click()