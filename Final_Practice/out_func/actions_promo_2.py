import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def action_promo_2(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[4]')).perform()
    logging.info('Наведён курсор на пиццу')
    time.sleep(3)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@data-product_id="425"])[1]').click()
    logging.info('Кликнута кнопка "В корзину"')
    time.sleep(2)

    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[6]')).perform()
    logging.info('Наведён курсор на пиццу')
    time.sleep(3)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@data-product_id="421"])[2]').click()
    logging.info('Кликнута кнопка "В корзину"')
    time.sleep(2)

    with allure.step('Открыта корзина'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/cart/"]').click()
    logging.info('Открыта корзина')
    time.sleep(2)

    with allure.step('Заполнено поле для промокода (неправильный промокод)'):
        browser.find_element(By.CSS_SELECTOR, '[name="coupon_code"]').send_keys('DC120')
    logging.info('Заполнено поле для промокода (неправильный промокод)')
    time.sleep(2)

    with allure.step('Промокод применён'):
        browser.find_element(By.CSS_SELECTOR, '[name="apply_coupon"]').click()
    logging.info('Промокод применён')
    time.sleep(2)

    promo_number = browser.find_element(By.XPATH, '(//*[@class="woocommerce-Price-amount amount"])[6]')
    with allure.step('Проверка суммы'):
        assert '950,00' in promo_number.text
    logging.info('Проверка суммы')

    message = browser.find_element(By.CSS_SELECTOR, '[class="woocommerce-error"]')
    with allure.step('Проверка сообщения'):
        assert 'Неверный купон.' in message.text
    logging.info('Проверка сообщения')