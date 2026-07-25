import time

from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page


class TestExample:
    def test_1(self, page: Page):
        page.goto('https://github.com/microsoft/vscode/issues')

        page.fill('css=[id="repository-input"]', 'in:title bug')
        page.keyboard.press('Enter')
        time.sleep(5)

        indexes = [3, 4, 5, 6, 8, 11, 15, 17, 18, 20, 22, 23, 30, 32, 33, 37, 39, 40, 41, 42, 43, 44, 50, 51, 52]

        for index in indexes:
            checking_task_name = page.locator(f'xpath=(//*[@class="prc-Text-Text-9mHv3"])[{index}]')
            expect(checking_task_name).to_contain_text('bug', ignore_case=True)

    def test_2(self, page: Page):
        page.goto('https://github.com/microsoft/vscode/issues')

        time.sleep(2)
        page.locator('[aria-label="Filter by author"] > span').click()

        time.sleep(5)
        page.fill('[placeholder="Filter authors"]', 'bpasero')

        time.sleep(3)
        page.locator('xpath=(//*[@class="prc-ActionList-ActionListContent-KBb8-"])[1]').click()

        time.sleep(3)

        indexes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

        for index in indexes:
            checking_autor = page.locator(f'xpath=(//*[@class="IssueItem-module__authorCreatedLink__YQP27 prc-Link-Link-9ZwDx"])[{index}]')
            expect(checking_autor).to_contain_text('bpasero')

    def test_3(self, page: Page):
        page.goto('https://github.com/search/advanced')

        page.locator('[id="search_language"]').click()

        for i in range(19):
            page.keyboard.press('ArrowDown')
        page.keyboard.press('Enter')

        page.fill('css=[id="search_stars"]', '>20000')

        page.fill('css=[id="search_filename"]', 'environment.yml')

        page.locator('xpath=(//*[@type="submit"])[4]').click()
        time.sleep(3)

        indexes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for index in indexes:
            checking_stars = page.locator(f'xpath=(//*[@class="Repositories-module__stargazersLink__TJh1w prc-Link-Link-9ZwDx"]//span)[{index}]').text_content()
            checking_stars = checking_stars[:3]
            checking_stars = int(checking_stars)
            assert checking_stars > 20

    def test_4(self, page: Page):
        page.goto('https://skillbox.ru/code/?type=profession')

        time.sleep(3)
        page.locator('[class="programs-filter-mobile__button programs-filter-mobile__button--desktop ui-button ui-button--stroke-secondary ui-button--medium ui-button--icon ui-button--icon-left"]').click()

        page.locator('xpath=//*[contains(text(), "От 6")]').click()

        page.locator('xpath=(//*[contains(text(), "Airflow")])[2]').click()

        page.locator('[class="ui-button ui-button--filled-main ui-button--small ui-button--''stretch"]').click()
        time.sleep(3)

        profession_indexes = [1, 2]

        for index in profession_indexes:
            checking_profession = page.locator(f'xpath=(//*[@class="product-card-new__direction f f--m f--14"])[{index}]')
            expect(checking_profession).to_contain_text('Профессия')

        continuance_indexes = [1, 3]

        for index in continuance_indexes:

            checking_continuance = page.locator(f'xpath=(//*[@class="product-card-new__feature f f--m f--14"])[{index}]')
            expect(checking_continuance).to_contain_text('месяцев')

            continuance = page.locator(f'xpath=(//*[@class="product-card-new__feature f f--m f--14"])[{index}]').text_content()
            continuance_num = ''
            for sym in continuance:
                if sym.isdigit():
                    continuance_num += sym
            continuance_num = int(continuance_num)
            assert continuance_num > 5

    def test_5(self, page: Page):
        page.goto('https://github.com/microsoft/vscode/graphs/commit-activity')


        time.sleep(3)
        element = page.locator('[aria-label="Sunday, 19 Jul 2026, 486. Commits."]')
        element.hover()

        date = page.locator('[style="color: var(--fgColor-muted, var(--color-fg-muted)); font-weight: var(--base-text-weight-semibold); padding-bottom: 2px;"]')

        expect(date).to_contain_text('Week of 19 Jul, 2026')

        commits = date.locator('xpath=(//strong)[3]')
        expect(commits).to_contain_text('486')