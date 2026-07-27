import allure

from Final_Practice.out_func.actions_promo_2 import action_promo_2


@allure.feature('Финальная работа')
@allure.story('Флоу с промокодом - Сценарий №2')
class Test_Promo_2:
    @allure.title('Применение неправильного промокода')
    def test_promo_2(self, browser):
        action_promo_2(self, browser)