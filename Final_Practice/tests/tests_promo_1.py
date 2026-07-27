import allure

from Final_Practice.out_func.actions_promo_1 import action_promo_1


@allure.feature('Финальная работа')
@allure.story('Флоу с промокодом - Сценарий №1')
class Test_Promo_1:
    @allure.title('Применение промокода')
    def test_promo_1(self, browser):
        action_promo_1(self, browser)