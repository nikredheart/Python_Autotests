import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class TestExample:
    def test_1(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        driver.find_element(By.CSS_SELECTOR, '[id="repository-input"]').send_keys('in:title bug' + Keys.ENTER)
        pass

    def test_2(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Filter by author"] > span').click()
        driver.find_element(By.CSS_SELECTOR, '[placeholder="Filter authors"]').send_keys('bpasero')
        driver.find_element(By.XPATH, '(//*[@class="prc-ActionList-ActionListContent-KBb8-"])[1]').click()
        pass

    def test_3(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/search/advanced')
        driver.find_element(By.CSS_SELECTOR, '[id="search_language"]').click()
        action_chains = webdriver.ActionChains(driver)
        for i in range(19):
            action_chains.send_keys(Keys.ARROW_DOWN).perform()
        action_chains.send_keys(Keys.ENTER).perform()
        driver.find_element(By.CSS_SELECTOR, '[id="search_stars"]').send_keys('>20000')
        driver.find_element(By.CSS_SELECTOR, '[id="search_filename"]').send_keys('environment.yml')
        driver.find_element(By.XPATH, '(//*[@type="submit"])[4]').click()
        pass

    def test_4(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://skillbox.ru/code/?type=profession')
        driver.find_element(By.CSS_SELECTOR, '[class="programs-filter-mobile__button programs-filter-mobile__button-'
                                             '-mobile ui-icon-button ui-icon-button--filled-secondary ui-icon-button-'
                                             '-medium ui-icon-button--square"]').click()
        driver.find_element(By.XPATH, '//*[contains(text(), "От 6")]').click()
        driver.find_element(By.XPATH, '(//*[contains(text(), "Airflow")])[2]').click()
        driver.find_element(By.CSS_SELECTOR, '[class="ui-button ui-button--filled-main ui-button--small ui-button--'
                                             'stretch"]').click()
        pass

    def test_5(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        action_chains = webdriver.ActionChains(driver)
        time.sleep(3)
        action_chains.move_to_element(driver.find_element(By.CSS_SELECTOR, '[aria-label="Sunday, 19 Apr 2026, 943. Commits."]')).perform()
        pass