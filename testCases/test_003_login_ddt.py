from pathlib import Path
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestLoginDDT:
    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    # Use pathlib for clean, cross-platform file path management
    excel_path = Path.cwd() / "testdata" / "Opencart_LoginData.xlsx"

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("**** Starting test_003_login_Datadriven *******")

        self.driver = setup
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)

        # Batch load data to reduce I/O overhead
        test_rows = XLUtils.get_all_rows(self.excel_path, "Sheet1")
        lst_status = []

        for row_idx, row in enumerate(test_rows, start=2):
            username, password, exp = row[0], row[1], str(row[2]).strip().lower()

            self.logger.info(
                f"Testing Row {row_idx}: User '{username}' | Expected result: '{exp}'"
            )

            # Reset state per iteration to prevent test pollution
            self.driver.get(self.base_url)

            # Navigate to Login Page
            self.hp.clickMyAccount()
            self.hp.clickLoginLink()

            # Perform Login
            self.lp.setUserName(username)
            self.lp.setPassword(password)
            self.lp.click_on_login_button()

            # Check page status
            target_page_exists = self.lp.isMyAccountPageExists()
            print(f"target_page_exists: {target_page_exists}")
            # Validation logic
            if exp == "valid":
                print(exp)
                if target_page_exists:
                    print(f"target_page_exists: {target_page_exists}")
                    self.logger.info(
                        f"Row {row_idx}: PASS (Valid user logged in)"
                    )
                    lst_status.append("Pass")
                    try:
                        print("Clicking on logout button")
                        self.hp.clickMyAccount()
                        self.hp.clickLogoutLink()
                    except Exception as e:
                        print("Exception: ", e)
                        self.logger.warning(
                            f"Row {row_idx}: Couldn't logout - {e}"
                        )
                else:
                    self.logger.error(
                        f"Row {row_idx}: FAIL (Valid user login failed)"
                    )
                    lst_status.append("Fail")

            elif exp == "invalid":
                if target_page_exists:
                    self.logger.error(
                        f"Row {row_idx}: FAIL (Invalid user logged in)"
                    )
                    lst_status.append("Fail")
                    try:
                        self.ma.click_logout_button()
                    except Exception as e:
                        self.logger.warning(
                            f"Row {row_idx}: Couldn't logout - {e}"
                        )
                else:
                    self.logger.info(
                        f"Row {row_idx}: PASS (Invalid user denied access)"
                    )
                    lst_status.append("Pass")

        # Pytest assertion
        assert (
            "Fail" not in lst_status
        ), f"DDT Test Failed! Execution Results: {lst_status}"
        self.logger.info("******* End of test_003_login_Datadriven **********")