import time
import logging

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def search_test_1(self, browser, website):
    with allure.step('Открыт сайт'):
        browser.get(website)
    logging.info('Открыт сайт')

    with allure.step('Поиск по заданному слову'):
        (browser.find_element(By.CSS_SELECTOR, '[id="repository-input"]').send_keys('in:title bug' + Keys.ENTER))
    logging.info('Выполнен поиск по заданному слову')
    time.sleep(5)


def check_test_1(self, browser):
    indexes = [3, 4, 7, 11, 12, 14, 21, 23, 27, 28, 29, 30, 31, 32, 33, 34, 35, 42, 43, 44, 45, 49, 52, 53, 54]

    with allure.step('Проверка наличия заданного слова'):
        for index in indexes:
            checking_task_name = (browser.find_element(By.XPATH, f'(//*[@class="prc-Text-Text-9mHv3"])[{index}]'))
            assert 'bug' in checking_task_name.text.lower()
    logging.info('Выполнена проверка наличия заданного слова')


def search_test_2(self, browser, website):
    with allure.step('Открыт сайт'):
        browser.get(website)
    logging.info('Открыт сайт')

    time.sleep(2)
    with allure.step('Нажата кнопка'):
        browser.find_element(By.CSS_SELECTOR, '[aria-label="Filter by author"] > span').click()
    logging.info('Нажата кнопка')
    time.sleep(5)

    with allure.step('Указано имя автора'):
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Filter authors"]').send_keys('bpasero')
    logging.info('Указано имя автора')
    time.sleep(3)

    with allure.step('Поиск по автору'):
        browser.find_element(By.XPATH, '(//*[@class="prc-ActionList-ActionListContent-KBb8-"])[1]').click()
    logging.info('Выполнен поиск по автору')
    time.sleep(3)


def check_test_2(self, browser):
    indexes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

    with allure.step('Проверка наличия имени автора'):
        for index in indexes:
            checking_author = (browser.find_element(By.XPATH,
                                                    f'(//*[@class="IssueItem-module__authorCreatedLink__Y'
                                                    f'QP27 prc-Link-Link-9ZwDx"])[{index}]'))
            assert 'bpasero' in checking_author.text.lower()
    logging.info('Выполнена проверка наличия имени автора')


def search_test_3(self, browser, website):
    with allure.step('Открыт сайт'):
        browser.get(website)
    logging.info('Открыт сайт')

    with allure.step('Выбран язык программирования'):
        browser.find_element(By.CSS_SELECTOR, '[id="search_language"]').click()

        action_chains = webdriver.ActionChains(browser)
        for i in range(19):
            action_chains.send_keys(Keys.ARROW_DOWN).perform()
        action_chains.send_keys(Keys.ENTER).perform()
    logging.info('Выбран язык программирования')

    with allure.step('Указано минимальное количество звёзд'):
        (browser.find_element(By.CSS_SELECTOR, '[id="search_stars"]').send_keys('>20000'))
    logging.info('Указано минимальное количество звёзд')

    with allure.step('Указан необходимый формат файла'):
        (browser.find_element(By.CSS_SELECTOR, '[id="search_filename"]').send_keys('environment.yml'))
    logging.info('Указан необходимый формат файла')

    with allure.step('Поиск'):
        browser.find_element(By.XPATH, '(//*[@type="submit"])[4]').click()
    logging.info('Выполнен поиск')
    time.sleep(3)


def check_test_3(self, browser):
    indexes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    with allure.step('Проверка соответствия количества звёзд'):
        for index in indexes:
            checking_stars = (browser.find_element(By.XPATH,
                                                   f'(//*[@class='
                                                   f'"Repositories-module__stargazersLink_'f'_'
                                                   f'KRMAf prc-Link-Link-9ZwDx"]//span)[{index}]'))
            stars = checking_stars.text
            stars = stars[:3]
            stars = int(stars)
            assert stars > 20
    logging.info('Выполнена проверка соответствия количества звёзд')


def search_test_4(self, browser, website):
    with allure.step('Открыт сайт'):
        browser.get(website)
    logging.info('Открыт сайт')

    time.sleep(3)
    with allure.step('Открыто окно с параметрами'):
        browser.find_element(By.CSS_SELECTOR,
                             '[class="programs-filter-mobile__button programs-filter-mobile__button-'
                             '-mobile ui-icon-button ui-icon-button--filled-secondary ui-icon-button-'
                             '-medium ui-icon-button--square"]').click()
    logging.info('Открыто окно с параметрами')

    with allure.step('Выбрана длительность'):
        browser.find_element(By.XPATH, '//*[contains(text(), "От 6")]').click()
    logging.info('Выбрана длительность')

    with allure.step('Выбрано направление'):
        browser.find_element(By.XPATH, '(//*[contains(text(), "Airflow")])[2]').click()
    logging.info('Выбрано направление')

    with allure.step('Параметры подтверждены'):
        browser.find_element(By.CSS_SELECTOR,
                             '[class="ui-button ui-button--filled-main ui-button--small ui-button--''stretch"]').click()
    logging.info('Параметры подтверждены')
    time.sleep(3)


def check_test_4(self, browser):
    profession_indexes = [1, 2]

    with allure.step('Проверка соответствия категории'):
        for index in profession_indexes:
            checking_profession = (
                browser.find_element(By.XPATH, f'(//*[@class="product-card-new__direction f f--m f--14"])[{index}]'))
            assert 'Профессия' in checking_profession.text
    logging.info('Выполнена проверка соответствия категории')

    continuance_indexes = [1, 3]

    with allure.step('Проверка соответствия длительности'):
        for index in continuance_indexes:
            checking_continuance = (
                browser.find_element(By.XPATH, f'(//*[@class="product-card-new__feature f f--m f--14"])[{index}]'))
            assert 'месяцев' in checking_continuance.text
            continuance = checking_continuance.text
            continuance_num = ''
            for sym in continuance:
                if sym.isdigit():
                    continuance_num += sym
            continuance_num = int(continuance_num)
            assert continuance_num > 5
    logging.info('Выполнена проверка соответствия длительности')


def search_test_5(self, browser, website):
    with allure.step('Открыт сайт'):
        browser.get(website)
    logging.info('Открыт сайт')

    action_chains = webdriver.ActionChains(browser)
    time.sleep(3)

    with allure.step('Курсор наведён на элемент'):
        action_chains.move_to_element(
            browser.find_element(By.CSS_SELECTOR, '[aria-label="Sunday, 19 Jul 2026, 365. Commits."]')).perform()
    logging.info('Курсор наведён на элемент')


def check_test_5(self, browser, required_date, required_commits):
    with allure.step('Проверка соответствия количества коммитов'):
        date = browser.find_element(By.CSS_SELECTOR,
                                    '[style="color: var(--fgColor-muted, var(--color-fg-muted)); font-weight: var(-'
                                    '-base-text-weight-semibold); padding-bottom: 2px;"]')
        assert required_date in date.text

        commits = date.find_element(By.XPATH, '(//strong)[3]')
        assert required_commits in commits.text
    logging.info('Выполнена проверка соответствия количества коммитов')