from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
import chromedriver_binary
import pytest

# Разные импорты


@pytest.fixture()
def set_up_browser(): # Настройки браузера
       options = ChromeOptions()
       driver = Chrome(options=options)
       yield driver
       driver.quit()