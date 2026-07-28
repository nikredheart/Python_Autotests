import allure

from Final_Practice.out_func.actions_main import *  # noqa: F403


@allure.feature('Финальная работа')
@allure.story('Основной флоу')
class Test_Main_Flow:
    @allure.title('Переход на сайт Pizzeria')
    def test_main_1(self, browser):
        action_main_1(self, browser)  # noqa: F405

    @allure.title('Добавление пиццы в корзину')
    def test_main_2(self, browser):  # ТЕСТ НЕ ЗАПУСКАЕТСЯ, ПРОБЛЕМЫ С САЙТОМ
        action_main_2(self, browser)  # noqa: F405

    @allure.title('Добавление в корзину пиццы, находящейся дальше по списку')
    def test_main_3(self, browser):  # ТЕСТ НЕ ЗАПУСКАЕТСЯ, ПРОБЛЕМЫ С САЙТОМ
        action_main_3(self, browser)  # noqa: F405

    @allure.title('Переход на страницу с подробной информацией о пицце')
    def test_main_4(self, browser):
        action_main_4(self, browser)  # noqa: F405

    @allure.title('Выбор дополнительных опций к пицце')
    def test_main_5(self, browser):  # ТЕСТ НЕ СРАБОТАЕТ, ЭЛЕМЕНТ НЕ СОДЕРЖИТ ИНФОРМАЦИЮ О ВЫБРАННОМ ЗНАЧЕНИИ
        action_main_5(self, browser)  # noqa: F405

    @allure.title('Добавление пиццы в корзину из страницы с информацией')
    def test_main_6(self, browser):
        action_main_6(self, browser)  # noqa: F405

    @allure.title('Переход в корзину кликом на кнопку в главном меню')
    def test_main_7(self, browser):
        action_main_7(self, browser)  # noqa: F405

    @allure.title('Проверка наличия выбранных пицц в корзине')
    def test_main_8(self, browser):
        action_main_8(self, browser)  # noqa: F405

    @allure.title('Увеличение количества пиццы в корзине')
    def test_main_9(self, browser):
        action_main_9(self, browser)  # noqa: F405

    @allure.title('Удаление пиццы из корзины')
    def test_main_10(self, browser):
        action_main_10(self, browser)  # noqa: F405

    @allure.title('Переход в раздел "Меню" - "Десерты" кликом на кнопку с выпадающим списком в главном меню')
    def test_main_11(self, browser):
        action_main_11(self, browser)  # noqa: F405

    @allure.title('Фильтрация десертов по цене')
    def test_main_12(self, browser):
        action_main_12(self, browser)  # noqa: F405

    @allure.title('Добавление десерта в корзину')
    def test_main_13(self, browser):
        action_main_13(self, browser)  # noqa: F405

    @allure.title('Проверка наличия десерта в корзине')
    def test_main_14(self, browser):
        action_main_14(self, browser)  # noqa: F405

    @allure.title('Переход к оформлению заказа кликом на кнопку "Перейти к оплате"')
    def test_main_15(self, browser):
        action_main_15(self, browser)  # noqa: F405

    @allure.title('Переход в страницу авторизации кликом на кнопку в главном меню')
    def test_main_16(self, browser):
        action_main_16(self, browser)  # noqa: F405

    @allure.title('Переход в страницу регистрации')
    def test_main_17(self, browser):
        action_main_17(self, browser)  # noqa: F405

    @allure.title('Регистрация')
    def test_main_18(self, browser):
        action_main_18(self, browser)  # noqa: F405

    @allure.title('Проверка успешной регистрации')
    def test_main_19(self, browser):
        action_main_19(self, browser)  # noqa: F405

    @allure.title('Продолжение оформления заказа')
    def test_main_20(self, browser):
        action_main_20(self, browser)  # noqa: F405

    @allure.title('Заполнение формы данными')
    def test_main_21(self, browser):  # ТЕСТ НЕ СРАБОТАЕТ, ЭЛЕМЕНТЫ НЕ СОДЕРЖАТ ИНФОРМАЦИЮ О УКАЗАННОМ ЗНАЧЕНИИ
        action_main_21(self, browser)  # noqa: F405

    @allure.title('Выбор даты оформления заказа')
    def test_main_22(self, browser):  # ТЕСТ НЕ СРАБОТАЕТ, ЭЛЕМЕНТ НЕ СОДЕРЖИТ ИНФОРМАЦИЮ О УКАЗАННОМ ЗНАЧЕНИИ
        action_main_22(self, browser)  # noqa: F405

    @allure.title('Выбор способа оплаты ("Оплата при доставке")')
    def test_main_23(self, browser):
        action_main_23(self, browser)  # noqa: F405

    @allure.title('Отметка чекбокса с принятием условий использования сайта')
    def test_main_24(self, browser):
        action_main_24(self, browser)  # noqa: F405

    @allure.title('Подтверждение заказа')
    def test_main_25(self, browser):
        action_main_25(self, browser)  # noqa: F405