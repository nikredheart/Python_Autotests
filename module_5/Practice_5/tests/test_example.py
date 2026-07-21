import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestExample:
    def test_1(self, browser):
        browser.get('https://github.com/microsoft/vscode/issues')

        (browser.find_element(By.CSS_SELECTOR, '[id="repository-input"]').send_keys('in:title bug' + Keys.ENTER))
        time.sleep(5)

        indexes = [4, 11, 13, 17, 18, 19, 21, 22, 23, 24, 25, 26, 33, 34, 35, 36, 38, 42, 45, 46, 47, 50, 51, 52, 55]

        for index in indexes:
            checking_task_name = (browser.find_element(By.XPATH, f'(//*[@class="prc-Text-Text-9mHv3"])[{index}]'))
            assert 'bug' in checking_task_name.text.lower()

    def test_2(self, browser):
        browser.get('https://github.com/microsoft/vscode/issues')

        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, '[aria-label="Filter by author"] > span').click()
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Filter authors"]').send_keys('bpasero')
        time.sleep(3)
        browser.find_element(By.XPATH, '(//*[@class="prc-ActionList-ActionListContent-KBb8-"])[1]').click()
        time.sleep(3)

        indexes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

        for index in indexes:
            checking_author = (browser.find_element(By.XPATH, f'(//*[@class="IssueItem-module__authorCreatedLink__YQP27 prc-Link-Link-9ZwDx"])[{index}]'))
            assert 'bpasero' in checking_author.text.lower()

    def test_3(self, browser):
        browser.get('https://github.com/search/advanced')

        browser.find_element(By.CSS_SELECTOR, '[id="search_language"]').click()

        action_chains = webdriver.ActionChains(browser)
        for i in range(19):
            action_chains.send_keys(Keys.ARROW_DOWN).perform()
        action_chains.send_keys(Keys.ENTER).perform()

        (browser.find_element(By.CSS_SELECTOR, '[id="search_stars"]').send_keys('>20000'))

        (browser.find_element(By.CSS_SELECTOR, '[id="search_filename"]').send_keys('environment.yml'))

        browser.find_element(By.XPATH, '(//*[@type="submit"])[4]').click()
        time.sleep(3)

        indexes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for index in indexes:
            checking_stars = (browser.find_element(By.XPATH, f'(//*[@class="Repositories-module__stargazersLink_'f'_KRMAf prc-Link-Link-9ZwDx"]//span)[{index}]'))
            stars = checking_stars.text
            stars = stars[:3]
            stars = int(stars)
            assert stars > 20

    def test_4(self, browser):
        browser.get('https://skillbox.ru/code/?type=profession')

        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, '[class="programs-filter-mobile__button programs-filter-mobile__button-''-mobile ui-icon-button ui-icon-button--filled-secondary ui-icon-button-''-medium ui-icon-button--square"]').click()

        # time.sleep(3)
        browser.find_element(By.XPATH, '//*[contains(text(), "От 6")]').click()

        # time.sleep(3)
        browser.find_element(By.XPATH, '(//*[contains(text(), "Airflow")])[2]').click()

        # time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, '[class="ui-button ui-button--filled-main ui-button--small ui-button--''stretch"]').click()
        time.sleep(3)

        profession_indexes = [1, 2]

        for index in profession_indexes:
            checking_profession = (browser.find_element(By.XPATH, f'(//*[@class="product-card-new__direction f f--m f--14"])[{index}]'))
            assert 'Профессия' in checking_profession.text

        continuance_indexes = [1, 3]

        for index in continuance_indexes:
            checking_continuance = (browser.find_element(By.XPATH, f'(//*[@class="product-card-new__feature f f--m f--14"])[{index}]'))
            assert 'месяцев' in checking_continuance.text
            continuance = checking_continuance.text
            contiance_num = ''
            for sym in continuance:
                if sym.isdigit():
                    contiance_num += sym
            contiance_num = int(contiance_num)
            assert contiance_num > 5

    def test_5(self, browser):
        browser.get('https://github.com/microsoft/vscode/graphs/commit-activity')

        action_chains = webdriver.ActionChains(browser)
        time.sleep(3)
        action_chains.move_to_element(
            browser.find_element(By.CSS_SELECTOR, '[aria-label="Sunday, 19 Jul 2026, 108. Commits."]')).perform()
        date = browser.find_element(By.CSS_SELECTOR, '[style="color: var(--fgColor-muted, var(--color-fg-muted)); font-weight: var(--base-text-weight-semibold); padding-bottom: 2px;"]')
        assert 'Week of 19 Jul, 2026' in date.text

        commits = date.find_element(By.XPATH, '(//strong)[3]')
        assert '108' in commits.text