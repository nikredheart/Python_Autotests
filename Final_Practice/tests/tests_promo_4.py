import allure

from Final_Practice.out_func.actions_promo_4 import action_promo_4


@allure.feature('Финальная работа')
@allure.story('Флоу с промокодом - Сценарий №4')
class Test_Promo_4:
    @allure.title('Применение ранее применявшегося промокода')
    def test_promo_4(self, browser):
        action_promo_4(self, browser)