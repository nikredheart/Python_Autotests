import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from urllib.parse import quote
import logging


def action_main_1(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')

    with allure.step('Проверка URL'):
        assert browser.current_url == 'https://pizzeria.skillbox.cc/'
    logging.info('Проверка URL')


def action_main_2(self, browser):
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
    with allure.step('Проверка текста кнопки'):
        button_1 = browser.find_element(By.XPATH, '(//*[@data-product_id="425"])[1]')
        assert 'ПОДРОБНЕЕ' in button_1.text
    logging.info('Проверка текста кнопки')
    time.sleep(2)

    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[6]')).perform()
    logging.info('Наведён курсор на пиццу')
    time.sleep(3)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@data-product_id="421"])[2]').click()
    logging.info('Кликнута кнопка "В корзину"')
    time.sleep(2)
    with allure.step('Проверка текста кнопки'):
        button_2 = browser.find_element(By.XPATH, '(//*[@data-product_id="421"])[2]')
        assert 'ПОДРОБНЕЕ' in button_2.text
    logging.info('Проверка текста кнопки')


def action_main_3(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[6]')).perform()
    logging.info('Наведён курсор на пиццу')

    with allure.step('Кликнута стрелка'):
        browser.find_element(By.CSS_SELECTOR, '[class="slick-next"]').click()
    logging.info('Кликнута стрелка')

    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[6]')).perform()
    logging.info('Наведён курсор на пиццу')
    time.sleep(2)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@href="?add-to-cart=419"])[2]').click()
    logging.info('Кликнута кнопка "В корзину"')
    time.sleep(2)
    with allure.step('Проверка текста кнопки'):
        button = browser.find_element(By.XPATH, '(//*[@href="?add-to-cart=419"])[2]')
        assert 'ПОДРОБНЕЕ' in button.text
    logging.info('Проверка текста кнопки')


def action_main_4(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[6]')).perform()
    logging.info('Наведён курсор на пиццу')

    with allure.step('Кликнута стрелка'):
        browser.find_element(By.CSS_SELECTOR, '[class="slick-next"]').click()
    logging.info('Кликнута стрелка')
    time.sleep(2)

    with allure.step('Открыта страница с информацией'):
        browser.find_element(By.XPATH, '(//*[@width="300"])[7]').click()
    logging.info('Открыта страница с информацией')

    with allure.step('Проверка URL'):
        url = 'https://pizzeria.skillbox.cc/product/пицца-ветчина-и-грибы/'
        browser.get(url)
        expected_encode = quote(url, safe=':/?&=')
        assert browser.current_url == expected_encode
    logging.info('Проверка URL')


def action_main_5(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[6]')).perform()
    logging.info('Наведён курсор на пиццу')

    with allure.step('Кликнута стрелка'):
        browser.find_element(By.CSS_SELECTOR, '[class="slick-next"]').click()
    logging.info('Кликнута стрелка')
    time.sleep(2)

    with allure.step('Открыта страница с информацией'):
        browser.find_element(By.XPATH, '(//*[@width="300"])[7]').click()
    logging.info('Открыта страница с информацией')

    with allure.step('Раскрыт список опций'):
        browser.find_element(By.ID, 'board_pack').click()
    logging.info('Раскрыт список опций')
    time.sleep(1)

    with allure.step('Выбрана опция'):
        browser.find_element(By.CSS_SELECTOR, '[value="55.00"]').click()
    logging.info('Выбрана опция')
    time.sleep(1)


def action_main_6(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[6]')).perform()
    logging.info('Наведён курсор на пиццу')

    with allure.step('Кликнута стрелка'):
        browser.find_element(By.CSS_SELECTOR, '[class="slick-next"]').click()
    logging.info('Кликнута стрелка')
    time.sleep(2)

    with allure.step('Открыта страница с информацией'):
        browser.find_element(By.XPATH, '(//*[@width="300"])[7]').click()
    logging.info('Открыта страница с информацией')
    time.sleep(2)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@type="submit"])[2]').click()
    logging.info('Кликнута кнопка "В корзину"')

    message = browser.find_element(By.CSS_SELECTOR, '[class="woocommerce-message"]')
    with allure.step('Проверка сообщения'):
        assert 'Вы отложили “Пицца «Ветчина и грибы»” в свою корзину.' in message.text
    logging.info('Проверка сообщения')


def action_main_7(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(2)

    with allure.step('Открыта корзина'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/cart/"]').click()
    logging.info('Открыта корзина')

    with allure.step('Проверка URL'):
        assert browser.current_url == 'https://pizzeria.skillbox.cc/cart/'
    logging.info('Проверка URL')


def action_main_8(self, browser):
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

    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[6]')).perform()
    logging.info('Наведён курсор на пиццу')
    time.sleep(3)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@data-product_id="421"])[2]').click()
    logging.info('Кликнута кнопка "В корзину"')

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[6]')).perform()
    logging.info('Наведён курсор на пиццу')

    with allure.step('Кликнута стрелка'):
        browser.find_element(By.CSS_SELECTOR, '[class="slick-next"]').click()
    logging.info('Кликнута стрелка')

    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[6]')).perform()
    logging.info('Наведён курсор на пиццу')
    time.sleep(2)

    with allure.step('Кликнута кнопка "В козину"'):
        browser.find_element(By.XPATH, '(//*[@href="?add-to-cart=419"])[2]').click()
    logging.info('Кликнута кнопка "В корзину"')

    with allure.step('Открыта страница с информацией'):
        browser.find_element(By.XPATH, '(//*[@width="300"])[7]').click()
    logging.info('Открыта страница с информацией')

    with allure.step('Раскрыт список с опциями'):
        browser.find_element(By.ID, 'board_pack').click()
    logging.info('Раскрыт список с опциями')
    time.sleep(1)

    with allure.step('Выбран тип опции'):
        browser.find_element(By.CSS_SELECTOR, '[value="55.00"]').click()
    logging.info('Выбран тип опции')
    time.sleep(2)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@type="submit"])[2]').click()
    logging.info('Кликнута кнопка "В корзину"')

    with allure.step('Открыта корзина'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/cart/"]').click()
    logging.info('Открыта корзина')

    with allure.step('Проверка корзины'):
        check_1 = browser.find_element(By.XPATH,
                                       '(//*[@href="http://pizzeria.skillbox.cc/product/'
                                       '%d0%bf%d0%b8%d1%86%d1%86%d0%b0-4-%d0%b2-1/"])[2]')
        assert 'Пицца "4 в 1"' in check_1.text
        check_2 = browser.find_element(By.XPATH,
                                       '(//*[@href="http://pizzeria.skillbox.cc/product/'
                                       '%d0%bf%d0%b8%d1%86%d1%86%d0%b0-%d1%80%d0%b0%d0%b9/"])[2]')
        assert 'Пицца "Рай"' in check_2.text
        check_3 = browser.find_element(By.XPATH,
                                       '(//*[@href="http://pizzeria.skillbox.cc/product/'
                                       '%d0%bf%d0%b8%d1%86%d1%86%d0%b0-%d0%b2%d0%b5%d1%82%d1%87%d0%b8%d0%bd%d0%b0-'
                                       '%d0%b8-%d0%b3%d1%80%d0%b8%d0%b1%d1%8b/"])[2]')
        assert 'Пицца "Ветчина и грибы"' in check_3.text
        check_4 = browser.find_element(By.XPATH, '// dl')
        assert 'Дополнительно:\nСырный борт' in check_4.text
    logging.info('Проверка корзины')


def action_main_9(self, browser):
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

    with allure.step('Открыта корзина'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/cart/"]').click()
    logging.info('Открыта корзина')

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Наведён курсор на поле с количеством'):
        action_chains.move_to_element(browser.find_element(By.CSS_SELECTOR, '[type="number"]')).perform()
    logging.info('Наведён курсор на поле с количеством')
    time.sleep(2)

    with allure.step('Увеличено значение'):
        browser.find_element(By.CSS_SELECTOR, '[type="number"]').send_keys(Keys.ARROW_UP)
    logging.info('Увеличено значение')

    with allure.step('Обновлена корзина'):
        browser.find_element(By.CSS_SELECTOR, '[value="Обновить корзину"]').click()
    logging.info('Обновлена корзина')
    time.sleep(3)

    message = browser.find_element(By.CSS_SELECTOR, '[class="woocommerce-message"]')
    time.sleep(1)
    with allure.step('Проверка сообщения'):
        assert 'Cart updated.' in message.text
    logging.info('Проверка сообщения')


def action_main_10(self, browser):
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

    with allure.step('Открыта корзина'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/cart/"]').click()
    logging.info('Открыта корзина')
    time.sleep(1)

    with allure.step('Пицца удалена'):
        browser.find_element(By.CSS_SELECTOR, '[class="remove"]').click()
    logging.info('Пицца удалена')
    time.sleep(2)

    message = browser.find_element(By.CSS_SELECTOR, '[class="woocommerce-message"]')
    with allure.step('Проверка сообщения'):
        assert '“Пицца "4 в 1"” удален.' in message.text
    logging.info('Проверка сообщения')


def action_main_11(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Раскрыт выпадающий список'):
        action_chains.move_to_element(
            browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/product-'
                                                  'category/menu/"]')).perform()
    logging.info('Раскрыт выпадающий список')
    time.sleep(1)

    with allure.step('Кликнута кнопка "Десерты"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/product-'
                                              'category/menu/deserts/"]').click()
    logging.info('Кликнута кнопка "Десерты"')

    with allure.step('Проверка URL'):
        assert browser.current_url == 'https://pizzeria.skillbox.cc/product-category/menu/deserts/'
    logging.info('Проверка URL')


def action_main_12(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Раскрыт выпадающий список'):
        action_chains.move_to_element(
            browser.find_element(By.CSS_SELECTOR,
                                 '[href="http://pizzeria.skillbox.cc/product-category/menu/"]')).perform()
    logging.info('Раскрыт выпадающий список')
    time.sleep(1)

    with allure.step('Кликнута кнопка "Десерты"'):
        browser.find_element(By.CSS_SELECTOR,
                             '[href="http://pizzeria.skillbox.cc/product-category/menu/deserts/"]').click()
    logging.info('Кликнута кнопка "Десерты"')
    time.sleep(1)

    slider = browser.find_element(By.XPATH, '(//*[@class="ui-slider-handle ui-state-default ui-corner-all"])[2]')
    action_chains = webdriver.ActionChains(browser)
    with allure.step('Передвинут слайдер'):
        action_chains.click_and_hold(slider).move_by_offset(xoffset=-150, yoffset=0).perform()
    action_chains.release().perform()
    logging.info('Передвинут слайдер')

    with allure.step('Изменения применены'):
        browser.find_element(By.XPATH, '(//*[@type="submit"])[2]').click()
    logging.info('Изменения применены')
    time.sleep(2)

    price_1 = browser.find_element(By.XPATH, '(//*[@class="woocommerce-Price-amount amount"])[1]')
    price_2 = browser.find_element(By.XPATH, '(//*[@class="woocommerce-Price-amount amount"])[2]')
    price_num_1 = price_1.text
    price_num_2 = price_2.text
    price_num_1 = int(price_num_1[:3])
    price_num_2 = int(price_num_2[:3])
    with allure.step('Проверка десертов на соответствие максимальной цене'):
        assert price_num_1 < 140
        assert price_num_2 < 140
    logging.info('Проверка десертов на соответствие максимальной цене')


def action_main_13(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Раскрыт выпадающий список'):
        action_chains.move_to_element(
            browser.find_element(By.CSS_SELECTOR,
                                 '[href="http://pizzeria.skillbox.cc/product-category/menu/"]')).perform()
    logging.info('Раскрыт выпадающий список')
    time.sleep(1)

    with allure.step('Кликнута кнопка "Десерты"'):
        browser.find_element(By.CSS_SELECTOR,
                             '[href="http://pizzeria.skillbox.cc/product-category/menu/deserts/"]').click()
    logging.info('Кликнута кнопка "Десерты"')
    time.sleep(1)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.CSS_SELECTOR, '[data-product_id="437"]').click()
    logging.info('Кликнута кнопка "В корзину"')
    time.sleep(2)

    button = browser.find_element(By.CSS_SELECTOR, '[class="added_to_cart wc-forward"]')
    with allure.step('Проверка текста кнопки'):
        assert 'ПОДРОБНЕЕ' in button.text
    logging.info('Проверка текста кнопки')


def action_main_14(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Раскрыт выпадающий список'):
        action_chains.move_to_element(
            browser.find_element(By.CSS_SELECTOR,
                                 '[href="http://pizzeria.skillbox.cc/product-category/menu/"]')).perform()
    logging.info('Раскрыт выпадающий список')
    time.sleep(1)

    with allure.step('Кликнута кнопка "Десерты"'):
        browser.find_element(By.CSS_SELECTOR,
                             '[href="http://pizzeria.skillbox.cc/product-category/menu/deserts/"]').click()
    logging.info('Кликнута кнопка "Десерты"')
    time.sleep(1)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.CSS_SELECTOR, '[data-product_id="437"]').click()
    logging.info('Кликнута кнопка "В корзину"')
    time.sleep(2)

    with allure.step('Открыта корзина'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/cart/"]').click()
    logging.info('Открыта корзина')

    check = browser.find_element(By.XPATH,
                                 '(//*[@class="product-name"])[2]')
    with allure.step('Проверка наличия в корзине десерта'):
        assert 'Десерт "Булочка с корицей"' in check.text
    logging.info('Проверка наличия в корзине десерта')


def action_main_15(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Раскрыт выпадающий список'):
        action_chains.move_to_element(
            browser.find_element(By.CSS_SELECTOR,
                                 '[href="http://pizzeria.skillbox.cc/product-category/menu/"]')).perform()
    logging.info('Раскрыт выпадающий список')
    time.sleep(1)

    with allure.step('Кликнута кнопка "Десерты"'):
        browser.find_element(By.CSS_SELECTOR,
                             '[href="http://pizzeria.skillbox.cc/product-category/menu/deserts/"]').click()
    logging.info('Кликнута кнопка "Десерты"')
    time.sleep(1)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.CSS_SELECTOR, '[data-product_id="437"]').click()
    logging.info('Кликнута кнопка "В корзину"')
    time.sleep(2)

    with allure.step('Открыта корзина'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/cart/"]').click()
    logging.info('Открыта корзина')
    time.sleep(2)

    with allure.step('Кликнута кнопка "Перейти к оплате"'):
        browser.find_element(By.XPATH, '(//*[@href="http://pizzeria.skillbox.cc/checkout/"])[2]').click()
    logging.info('Кликнута кнопка "Перейти к оплате"')
    time.sleep(2)

    message_1 = browser.find_element(By.XPATH, '(//*[@class="woocommerce-info"])[1]')
    message_2 = browser.find_element(By.XPATH, '(//*[@class="woocommerce-info"])[2]')
    with allure.step('Проверка сообщений'):
        assert 'Зарегистрированы на сайте?' in message_1.text
        assert 'Есть купон?' in message_2.text
    logging.info('Проверка сообщений')


def action_main_16(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(2)

    with allure.step('Открыта страница "Мой аккаунт"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/my-account/"]').click()
    logging.info('Открыта страница "Мой аккаунт"')

    title = browser.find_element(By.CSS_SELECTOR, '[class="post-title"]')
    with allure.step('Проверка заголовка'):
        assert 'МОЙ АККАУНТ' in title.text
    logging.info('Проверка заголовка')


def action_main_17(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(2)

    with allure.step('Открыта страница "Мой аккаунт"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/my-account/"]').click()
    logging.info('Открыта страница "Мой аккаунт"')

    title = browser.find_element(By.CSS_SELECTOR, '[class="post-title"]')
    with allure.step('Кликнута кнопка "Зарегистрироваться"'):
        browser.find_element(By.CSS_SELECTOR, '[class="custom-register-button"]').click()
    logging.info('Кликнута кнопка "Зарегистрироваться"')

    title = browser.find_element(By.CSS_SELECTOR, '[class="post-title"]')
    with allure.step('Проверка заголовка'):
        assert 'РЕГИСТРАЦИЯ' in title.text
    logging.info('Проверка заголовка')


def action_main_18(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(2)

    with allure.step('Открыта страница "Мой аккаунт"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/my-account/"]').click()
    logging.info('Открыта страница "Мой аккаунт"')

    title = browser.find_element(By.CSS_SELECTOR, '[class="post-title"]')
    with allure.step('Кликнута кнопка "Зарегистрироваться"'):
        browser.find_element(By.CSS_SELECTOR, '[class="custom-register-button"]').click()
    logging.info('Кликнута кнопка "Зарегистрироваться"')

    title = browser.find_element(By.CSS_SELECTOR, '[class="post-title"]')
    with allure.step('Заполнено поле "Имя"'):
        browser.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys('Andrew Testermansen')
    logging.info('Заполнено поле "Имя"')

    with allure.step('Заполнено поле "Адрес почты"'):
        browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('xtestandre@test.ru')
    logging.info('Заполнено поле "Адрес почты"')

    with allure.step('Заполнено поле "Пароль"'):
        browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('password')
    logging.info('Заполнено поле "Пароль"')

    with allure.step('Кликнута кнопка "Зарегистрироваться"'):
        browser.find_element(By.CSS_SELECTOR, '[name="register"]').click()
    logging.info('Кликнута кнопка "Зарегистрироваться"')
    time.sleep(3)

    title = browser.find_element(By.CSS_SELECTOR, '[class="post-title"]')
    with allure.step('Проверка заголовка'):
        assert 'РЕГИСТРАЦИЯ' in title.text
    logging.info('Проверка заголовка')

    message = browser.find_element(By.CSS_SELECTOR, '[class="content-page"]')
    with allure.step('Проверка сообщения'):
        assert 'Регистрация завершена' in message.text
    logging.info('Проверка сообщения')


def action_main_19(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(2)

    with allure.step('Открыта страница "Мой аккаунт"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/my-account/"]').click()
    logging.info('Открыта страница "Мой аккаунт"')

    with allure.step('Заполнено поле "Имя"'):
        browser.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys('Andrew Testermansen')
    logging.info('Заполнено поле "Имя"')

    with allure.step('Заполнено поле "Пароль"'):
        browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('password')
    logging.info('Заполнено поле "Пароль"')

    with allure.step('Выполнен вход'):
        browser.find_element(By.XPATH, '(//*[@type="submit"])[2]').click()
    logging.info('Выполнен вход')
    time.sleep(2)

    title = browser.find_element(By.CSS_SELECTOR, '[class="post-title"]')
    with allure.step('Проверка заголовка'):
        assert 'МОЙ АККАУНТ' in title.text
    logging.info('Проверка заголовка')

    greeting = browser.find_element(By.CSS_SELECTOR, '[class="content-page"] p')
    with allure.step('Проверка приветствия'):
        assert 'Привет Andrew Testermansen' in greeting.text
    logging.info('Проверка приветствия')


def action_main_20(self, browser):
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

    with allure.step('Открыта корзина'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/cart/"]').click()
    logging.info('Открыта корзина')
    time.sleep(2)

    with allure.step('Кликнута кнопка "Перейти к оплате"'):
        browser.find_element(By.XPATH, '(//*[@href="http://pizzeria.skillbox.cc/checkout/"])[2]').click()
    logging.info('Кликнута кнопка "Перейти к оплате"')
    time.sleep(2)

    title = browser.find_element(By.CSS_SELECTOR, '[class="post-title"]')
    with allure.step('Проверка заголовка'):
        assert 'ОФОРМЛЕНИЕ ЗАКАЗА' in title.text
    logging.info('Проверка заголовка')


def action_main_21(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    with allure.step('Открыта страница "Мой аккаунт"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/my-account/"]').click()
    logging.info('Открыта страница "Мой аккаунт"')

    with allure.step('Заполнено поле "Имя"'):
        browser.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys('Andrew Testermansen')
    logging.info('Заполнено поле "Имя"')

    with allure.step('Заполнено поле "Пароль"'):
        browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('password')
    logging.info('Заполнено поле "Пароль"')

    with allure.step('Выполнен вход'):
        browser.find_element(By.XPATH, '(//*[@type="submit"])[2]').click()
    logging.info('Выполнен вход')
    time.sleep(2)

    with allure.step('Открыта главная страница'):
        browser.find_element(By.XPATH, '(//*[@href="http://pizzeria.skillbox.cc/"])[3]').click()
    logging.info('Открыта главная страница')
    time.sleep(1)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[4]')).perform()
    logging.info('Наведён курсор на пиццу')
    time.sleep(3)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@data-product_id="425"])[1]').click()
    logging.info('Кликнута кнопка "В корзину"')
    time.sleep(2)

    with allure.step('Кликнута кнопка "Перейти к оплате"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/checkout/"]').click()
    logging.info('Кликнута кнопка "Перейти к оплате"')
    time.sleep(2)

    with allure.step('Заполнено поле "Имя"'):
        browser.find_element(By.CSS_SELECTOR, '[id="billing_first_name"]').send_keys('Андрей')
    logging.info('Заполнено поле "Имя"')

    with allure.step('Заполнено поле "Фамилия"'):
        browser.find_element(By.CSS_SELECTOR, '[id="billing_last_name"]').send_keys('Тестировщик')
    logging.info('Заполнено поле "Фамилия"')

    with allure.step('Заполнено поле "Адрес"'):
        browser.find_element(By.CSS_SELECTOR, '[id="billing_address_1"]').send_keys('ул. Тестировщиков, 22')
    logging.info('Заполнено поле "Адрес"')

    with allure.step('Заполнено поле "Город / Населённый пункт"'):
        browser.find_element(By.CSS_SELECTOR, '[id="billing_city"]').send_keys('г. Тестерград')
    logging.info('Заполнено поле "Город / Населённый пункт"')

    with allure.step('Заполено поле "Область"'):
        browser.find_element(By.CSS_SELECTOR, '[id="billing_state"]').send_keys('Тестерградская обл.')
    logging.info('Заполнено поле "Область"')

    with allure.step('Заполнено поле "Индекс"'):
        browser.find_element(By.CSS_SELECTOR, '[id="billing_postcode"]').send_keys('22777')
    logging.info('Заполнено поле "Индекс"')

    with allure.step('Заполено поле "Телефон"'):
        browser.find_element(By.CSS_SELECTOR, '[id="billing_phone"]').send_keys('+77777777777')
    logging.info('Заполнено поле "Телефон"')


def action_main_22(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    with allure.step('Открыта страница "Мой аккаунт"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/my-account/"]').click()
    logging.info('Открыта страница "Мой аккаунт"')

    with allure.step('Заполнено поле "Имя"'):
        browser.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys('Andrew Testermansen')
    logging.info('Заполнено поле "Имя"')

    with allure.step('Заполнено поле "Пароль"'):
        browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('password')
    logging.info('Заполнено поле "Пароль"')

    with allure.step('Выполнен вход"'):
        browser.find_element(By.XPATH, '(//*[@type="submit"])[2]').click()
    logging.info('Выполнен вход')
    time.sleep(2)

    with allure.step('Открыта главная страница'):
        browser.find_element(By.XPATH, '(//*[@href="http://pizzeria.skillbox.cc/"])[3]').click()
    logging.info('Открыта главная страница')
    time.sleep(1)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[4]')).perform()
    logging.info('Наведён курсор на пиццу')
    time.sleep(3)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@data-product_id="425"])[1]').click()
    logging.info('Кликнута кнопка "В корзину"')
    time.sleep(2)

    with allure.step('Открыта страница "Оформление заказа"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/checkout/"]').click()
    logging.info('Открыта страница "Оформление заказа"')
    time.sleep(2)

    with allure.step('Указана дата заказа'):
        browser.find_element(By.CSS_SELECTOR, '[id="order_date"]').send_keys('27072026')
    logging.info('Указана дата заказа')


def action_main_23(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')

    time.sleep(3)
    with allure.step('Открыта страница "Мой аккаунт"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/my-account/"]').click()
    logging.info('Открыта страница "Мой акаунт"')

    with allure.step('Заполнено поле "Имя"'):
        browser.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys('Andrew Testermansen')
    logging.info('Заполнено поле "Имя"')

    with allure.step('Заполнено поле "Пароль"'):
        browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('password')
    logging.info('Заполнено поле "Пароль"')

    with allure.step('Выполнен вход"'):
        browser.find_element(By.XPATH, '(//*[@type="submit"])[2]').click()
    logging.info('Выполнен вход')
    time.sleep(2)

    with allure.step('Открыта главная страница'):
        browser.find_element(By.XPATH, '(//*[@href="http://pizzeria.skillbox.cc/"])[3]').click()
    logging.info('Открыта главная страница')
    time.sleep(1)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[4]')).perform()
    logging.info('Наведён курсор на пиццу')
    time.sleep(3)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@data-product_id="425"])[1]').click()
    logging.info('Кликнута кнопка "В корзину"')
    time.sleep(2)

    with allure.step('Открыта страница "Оформление заказа"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/checkout/"]').click()
    logging.info('Открыта страница "Оформление заказа"')
    time.sleep(2)

    with allure.step('Кликнут радиобаттон'):
        browser.find_element(By.CSS_SELECTOR, '[id="payment_method_cod"]').click()
    logging.info('Кликнут радиобаттон')
    time.sleep(1)

    with allure.step('Проверка описания'):
        descript = browser.find_element(By.CSS_SELECTOR, '[class="payment_box payment_method_cod"]')
    assert 'Оплата наличными при доставке заказа.' in descript.text
    logging.info('Проверка описания')


def action_main_24(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    with allure.step('Открыта страница "Мой аккаунт"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/my-account/"]').click()
    logging.info('Открыта страница "мой аккаунт"')

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

    with allure.step('Открыта главная страница'):
        browser.find_element(By.XPATH, '(//*[@href="http://pizzeria.skillbox.cc/"])[3]').click()
    logging.info('Открыта главная страница')
    time.sleep(1)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[4]')).perform()
    logging.info('Наведён курсор на пиццу')
    time.sleep(3)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@data-product_id="425"])[1]').click()
    logging.info('Кликнута кнопка "В корзину"')
    time.sleep(2)

    with allure.step('Открыта страница "Оформление заказа"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/checkout/"]').click()
    logging.info('Открыта страница "Оформление заказа"')
    time.sleep(2)

    with allure.step('Отмечен чекбокс'):
        browser.find_element(By.CSS_SELECTOR, '[id="terms"]').click()
    logging.info('Отмечен чекбокс')

    with allure.step('Проверка отметки чекбокса'):
        browser.find_element(By.CSS_SELECTOR, '[class="form-row validate-required woocommerce-validated"]')
    logging.info('роверка отметки чекбокса')


def action_main_25(self, browser):
    with allure.step('Открыт сайт'):
        browser.get('https://pizzeria.skillbox.cc/')
    logging.info('Открыт сайт')
    time.sleep(3)

    with allure.step('Открыта страница "Мой аккаунт"'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/my-account/"]').click()
    logging.info('Открыта страница "Мой аккаунт"')

    with allure.step('Заполнено поле "Имя"'):
        browser.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys('Andrew Testermansen')
    logging.info('Заполнено поле "Имя"')

    with allure.step('Заполено поле "Пароль"'):
        browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('password')
    logging.info('Заполнено поле "Пароль"')

    with allure.step('Выполнен вход'):
        browser.find_element(By.XPATH, '(//*[@type="submit"])[2]').click()
    logging.info('Выполнен вход')
    time.sleep(2)

    with allure.step('Открыта главная страница'):
        browser.find_element(By.XPATH, '(//*[@href="http://pizzeria.skillbox.cc/"])[3]').click()
    logging.info('Открыта главная страница')
    time.sleep(1)

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[4]')).perform()
    logging.info('Наведён куроср на пиццу')
    time.sleep(3)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@data-product_id="425"])[1]').click()
    logging.info('Кликнута кнопка "В корзину"')

    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[6]')).perform()
    logging.info('Наведён курсор на пиццу')
    time.sleep(3)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@data-product_id="421"])[2]').click()
    logging.info('Кликнута кнопка "В корзину"')

    action_chains = webdriver.ActionChains(browser)
    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[6]')).perform()
    logging.info('Наведён курсор на пиццу')

    with allure.step('Кликнута стрелка'):
        browser.find_element(By.CSS_SELECTOR, '[class="slick-next"]').click()
    logging.info('Кликнута стрелка')

    with allure.step('Наведён курсор на пиццу'):
        action_chains.move_to_element(browser.find_element(By.XPATH, '(//*[@width="300"])[6]')).perform()
    logging.info('Наведён курсор на пиццу')
    time.sleep(2)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@href="?add-to-cart=419"])[2]').click()
    logging.info('Кликнута кнопка "В корзину"')

    with allure.step('Открыта страница с информацией'):
        browser.find_element(By.XPATH, '(//*[@width="300"])[7]').click()
    logging.info('Открыта страница с информацией')

    with allure.step('Раскрыт список опций'):
        browser.find_element(By.ID, 'board_pack').click()
    logging.info('Раскрыт список опций')
    time.sleep(1)

    with allure.step('Выбран тип опции'):
        browser.find_element(By.CSS_SELECTOR, '[value="55.00"]').click()
    logging.info('Выбран тип опции')
    time.sleep(2)

    with allure.step('Кликнута кнопка "В корзину"'):
        browser.find_element(By.XPATH, '(//*[@type="submit"])[2]').click()
    logging.info('Кликнута кнопка "В корзину"')
    time.sleep(1)

    with allure.step('Открыта корзина'):
        browser.find_element(By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/cart/"]').click()
    logging.info('Открыта корзина')
    time.sleep(2)

    with allure.step('Кликнута кнопка "Перейти к оплате"'):
        browser.find_element(By.XPATH, '(//*[@href="http://pizzeria.skillbox.cc/checkout/"])[2]').click()
    logging.info('Кликнута кнопка "Перейти к оплате"')
    time.sleep(2)

    with allure.step('Заполнено поле "Имя"'):
        browser.find_element(By.CSS_SELECTOR, '[id="billing_first_name"]').send_keys('Андрей')
    logging.info('Заполнено поле "Имя"')

    with allure.step('Заполнено поле "Фамилия"'):
        browser.find_element(By.CSS_SELECTOR, '[id="billing_last_name"]').send_keys('Тестировщик')
    logging.info('Заполнено поле "Фамилия"')

    with allure.step('Заполнено поле "Адрес"'):
        browser.find_element(By.CSS_SELECTOR, '[id="billing_address_1"]').send_keys('ул. Тестировщиков, 22')
    logging.info('Заполнено поле "Адрес"')

    with allure.step('Заполнено поле "Город / Населённый пункт"'):
        browser.find_element(By.CSS_SELECTOR, '[id="billing_city"]').send_keys('г. Тестерград')
    logging.info('Заполнено поле "Город / Населённый пункт"')

    with allure.step('Заполнено поле "Область"'):
        browser.find_element(By.CSS_SELECTOR, '[id="billing_state"]').send_keys('Тестерградская обл.')
    logging.info('Заполнено поле "Область"')

    with allure.step('Заполнено поле "Почтовый индекс"'):
        browser.find_element(By.CSS_SELECTOR, '[id="billing_postcode"]').send_keys('22777')
    logging.info('Заполнено поле "Почтовый индекс"')

    with allure.step('Заполнено поле "Номер"'):
        browser.find_element(By.CSS_SELECTOR, '[id="billing_phone"]').send_keys('+77777777777')
    logging.info('Заполнено поле "Номер"')

    with allure.step('Указана дата заказа'):
        browser.find_element(By.CSS_SELECTOR, '[id="order_date"]').send_keys('27072026')
    logging.info('Указана дата заказа')

    with allure.step('Отмечен чекбокс'):
        browser.find_element(By.CSS_SELECTOR, '[id="terms"]').click()
    logging.info('Отмечен чекбокс')

    with allure.step('Кликнут радиобаттон'):
        browser.find_element(By.CSS_SELECTOR, '[class="button alt"]').click()
    logging.info('Кликнут радиобаттон')
    time.sleep(3)

    name = browser.find_element(By.CSS_SELECTOR, 'address')
    with allure.step('Проверка данных'):
        assert 'Андрей Тестировщик\nул. Тестировщиков, 22\nг. Тестерград\nТестерградская обл.\n22777' in name.text
    logging.info('Проверка данных')

    number = browser.find_element(By.CSS_SELECTOR, '[class="woocommerce-customer-details--phone"]')
    with allure.step('Проверка номера'):
        assert '+77777777777' in number.text
    logging.info('Проверка номера')

    mail = browser.find_element(By.CSS_SELECTOR, '[class="woocommerce-customer-details--email"]')
    with allure.step('Проверка адреса почты'):
        assert 'xtestandre@test.ru' in mail.text
    logging.info('Проверка адреса почты')