from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
import chromedriver_binary  # noqa: F401
import pytest
import logging


@pytest.fixture()
def browser():
        options = ChromeOptions()
        logging.info('Preparing the browser...')
        driver = Chrome(options=options)
        logging.info('The browser is ready!')
        yield driver
        driver.quit()