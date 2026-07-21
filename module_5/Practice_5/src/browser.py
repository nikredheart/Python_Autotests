from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
import chromedriver_binary
import pytest


@pytest.fixture()
def browser():
       options = ChromeOptions()
       driver = Chrome(options=options)
       yield driver
       driver.quit()