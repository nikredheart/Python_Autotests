import allure


@allure.feature('Финальная работа')
@allure.story('Флоу с промокодом - Сценарий №3')
class Test_Promo_3:
    @allure.title('Применение промокода с блокировкой запроса')
    def test_promo_3(self, browser):
        pass