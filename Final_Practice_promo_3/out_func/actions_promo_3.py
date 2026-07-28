import time

import allure
from playwright.sync_api import Page, expect
import logging


def action_promo_3(self, page: Page):
    with allure.step('Открыт сайт'):
        page.goto('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    element = page.locator('xpath=(//*[@width="300"])[5]')
    with allure.step('Наведён курсор на пиццу'):
        element.hover()
    logging.info('Наведён курсор на пиццу')
    time.sleep(3)

    with allure.step('Кликнута кнопка "В корзину"'):
        page.locator('xpath=(//*[@data-product_id="425"])[1]').click()
    logging.info('Кликнута кнопка "В корзину"')
    time.sleep(2)

    with allure.step('Открыта корзина'):
        page.locator('[id="menu-item-29"]').click()
    logging.info('Открыта корзина')
    time.sleep(2)

    with allure.step('В поле введён промокод'):
        page.fill('[name="coupon_code"]', 'GIVEMEHALYAVA')
    logging.info('В поле введён промокод')
    time.sleep(2)

    with allure.step('Запрос заблокирован'):
        page.route("**/?wc-ajax=apply_coupon", lambda route: route.abort())
    logging.info('Запрос заблокирован')

    with allure.step('Промокод применён'):
        page.locator('[name="apply_coupon"]').click()
    logging.info('Промокод применён')

    message = page.locator('[class="woocommerce-message"]')
    with allure.step('Проверка сообщения об ошибке'):
        expect(message).to_contain_text('Network ERROR: 505')
    logging.info('Проверка сообщения об ошибке')

    price = page.locator('xpath=(//*[@class="woocommerce-Price-amount amount"])[4]')
    with allure.step('Проверка суммы'):
        expect(price).to_contain_text('435,00')
    logging.info('Проверка суммы')