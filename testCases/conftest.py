from datetime import datetime
import os
import re
import pytest
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser options: chrome, edge, firefox",
    )


@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")

    if browser.lower() == "chrome":
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)

    elif browser.lower() == "edge":
        options = EdgeOptions()
        driver = webdriver.Edge(options=options)

    elif browser.lower() == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


# Single merged configure hook: handles report output location & environment metadata
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Set dynamic HTML report path with timestamp
    reports_dir = os.path.join(os.curdir, "reports")
    os.makedirs(reports_dir, exist_ok=True)

    time_stamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    config.option.htmlpath = os.path.abspath(
        os.path.join(reports_dir, f"report_{time_stamp}.html")
    )

    # Set metadata for HTML report
    if hasattr(config, "_metadata"):
        config._metadata["Project Name"] = "Opencart"
        config._metadata["Module Name"] = "CustRegistration"
        config._metadata["Tester"] = "Mahesh"


# Remove unwanted default metadata items from report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


# Take screenshot on failure and embed it directly into the HTML report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")

        if driver:
            # 1. Create screenshots directory
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            # 2. Sanitize filename (handles parameterized tests safely)
            safe_nodeid = re.sub(r"[^\w\-_.]", "_", report.nodeid)
            screenshot_path = os.path.join(
                screenshot_dir, f"{safe_nodeid}.png"
            )

            # 3. Save screenshot on disk
            driver.save_screenshot(screenshot_path)

            # 4. Attach screenshot to pytest-html report
            if os.path.exists(screenshot_path):
                html_embed = (
                    f'<div><img src="{screenshot_path}" alt="screenshot" '
                    f'style="width:300px; height:auto; margin:10px 0;" '
                    f'onclick="window.open(this.src)"/></div>'
                )
                extra.append(extras.html(html_embed))

    report.extra = extra
    