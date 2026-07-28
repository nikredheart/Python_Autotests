import allure

from Final_Practice_promo_3.out_func.actions_promo_3 import action_promo_3


@allure.feature('Финальная работа')
@allure.story('Флоу с промокодом - Сценарий №3')
class Test_Promo_3:
    @allure.title('Применение промокода с блокировкой запроса')
    def test_promo_3(self, page):
        action_promo_3(self, page)