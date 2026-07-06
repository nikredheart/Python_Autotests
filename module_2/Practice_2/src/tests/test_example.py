class TestExample: # Тестовый набор для проверки сайта skillbox.ru
       def test_example(self, set_up_browser): # Тест, проверяющий заголовок
              driver = set_up_browser
              driver.get('https://skillbox.ru')
              assert 'Skillbox – образовательная платформа с онлайн-курсами.' == driver.title