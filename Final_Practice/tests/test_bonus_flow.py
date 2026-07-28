import allure

from Final_Practice.out_func.actions_bonus import *  # noqa: F403


@allure.feature('Финальная работа')
@allure.story('Флоу с бонусной системой')
class Test_Bonus_Flow:
    @allure.title('Переход на страницу бонусной программы')
    def test_bonus_1(self, browser):
        action_bonus_1(self, browser)  # noqa: F405

    @allure.title('Оформление карты')
    def test_bonus_2(self, browser):
        action_bonus_2(self, browser)  # noqa: F405