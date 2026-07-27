from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
import chromedriver_binary  # noqa
import pytest
import logging


@pytest.fixture()
def browser():
    options = ChromeOptions()
    logging.info('Подготовка браузера...')
    driver = Chrome(options=options)
    logging.info('Браузер готов к работе')
    yield driver
    driver.quit()