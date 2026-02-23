from deepdiff import DeepDiff
import allure
from playwright.sync_api import Page, expect


class BasePage:
    base_url= 'https://www.saucedemo.com/'

    def __init__(self, page: Page):
        self.page = page

    def open_base_page(self):
        with allure.step(f'Открыть страницу с url{self.base_url}'):
            self.page.goto(self.base_url)

    @staticmethod
    def compare_count_in_cart_and_random(items, random_count):
        with allure.step('сравнить количество элементов на странице корзины с количеством добавленных'):
            expect(items).to_have_count(int(random_count))

    @staticmethod
    def check_url(self, url):
        with allure.step(f'Url страницы должен быть равен {url}'):
            expect(self.page).to_have_url(url)

    @staticmethod
    def check_the_match_of_these_elements(first, second):
        with allure.step('Проверить совпадают ли данные элементов'):
            diff = DeepDiff(first, second, ignore_order=True)
            assert not diff, f"Найдена разница: {diff}"