import pytest
import selenium.webdriver as webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    return driver

