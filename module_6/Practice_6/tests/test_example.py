import allure

from module_6.Practice_6.out_funcs.actions import * # noqa


@allure.feature('module_6')
@allure.story('Practice_6')
class TestExample:
    @allure.title('Проверка наличия слова "баг" в заголовках задач')
    def test_1(self, browser):
        search_test_1(self, browser, website='https://github.com/microsoft/vscode/issues')  # noqa: F405
        check_test_1(self, browser)  # noqa: F405

    @allure.title('Проверка принадлежности всех задач указанному автору')
    def test_2(self, browser):
        search_test_2(self, browser, website='https://github.com/microsoft/vscode/issues')  # noqa: F405
        check_test_2(self, browser)  # noqa: F405

    @allure.title('Проверка соответствия количества звёзд указанному значению')
    def test_3(self, browser):
        search_test_3(self, browser, website='https://github.com/search/advanced')  # noqa: F405
        check_test_3(self, browser)  # noqa: F405

    @allure.title('Проверка соответствия курсов заданным параметрам')
    def test_4(self, browser):
        search_test_4(self, browser, website='https://skillbox.ru/code/?type=profession')  # noqa: F405
        check_test_4(self, browser)  # noqa: F405

    @allure.title('Проверка отображения требуемых значений в тултипе')
    def test_5(self, browser):
        search_test_5(self, browser, website='https://github.com/microsoft/vscode/graphs/commit-activity')  # noqa: F405
        check_test_5(self, browser, required_date='Week of 19 Jul, 2026', required_commits='484')  # noqa: F405