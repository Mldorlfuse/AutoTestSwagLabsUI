import allure
from playwright.sync_api import Page

class BasePage:
    base_url= 'https://www.saucedemo.com/'

    def __init__(self, page: Page):
        self.page = page

    def open_base_page(self):
        with allure.step(f'Открыть страницу с url{self.base_url}'):
            self.page.goto(self.base_url)