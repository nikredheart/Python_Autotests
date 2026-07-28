import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import logging


def action_bonus_1(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(2)

    with allure.step('Открыта страница "Бонусная программа"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/bonus/"]').click()
    logging.info('Открыта страница "Бонусная программа"')

    with allure.step('Проверка URL'):
        assert browser.current_url == 'https://pizzeria.skillbox.cc/bonus/'
    logging.info('Проверка URL')


def action_bonus_2(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    with allure.step('Открыта страница "Мой аккаунт"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/my-account/"]').click()
    logging.info('Открыта страница "Мой аккаунт"')

    with allure.step('Заполнено поле "Имя"'):
        browser.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys('Andrew Testerman')
    logging.info('Заполнено поле "Имя"')

    with allure.step('Заполнено поле "Пароль"'):
        browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('password')
    logging.info('Заполнено поле "Пароль"')

    with allure.step('Выполнен вход'):
        browser.find_element(By.XPATH, '(//*[@type="submit"])[2]').click()
    logging.info('Выполнен вход')
    time.sleep(2)

    with allure.step('Открыта страница "Бонусная программа"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/bonus/"]').click()
    logging.info('Открыта страница "Бонусная программа"')

    with allure.step('Заполнено поле "Имя"'):
        browser.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys('Андрей')
    logging.info('Заполнено поле "Имя"')

    with allure.step('Заполнено поле "Телефон"'):
        browser.find_element(By.CSS_SELECTOR, '[id="bonus_phone"]').send_keys('+77777777777')
    logging.info('Заполнено поле "Телефон"')

    with allure.step('Кликнута кнопка оформления'):
        browser.find_element(By.CSS_SELECTOR, '[name="bonus"]').click()
    logging.info('Кликнута кнопка оформления')
    time.sleep(3)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Закрыто окно с уведомлением'):
        action_chains.send_keys(Keys.ESCAPE).perform()
    logging.info('Закрыто окно с уведомлением')

    pass  # До устранения проблемы с сайтом дальнейшая разработка теста невозможна