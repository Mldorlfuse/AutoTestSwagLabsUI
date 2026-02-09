import allure
from playwright.sync_api import Page, expect

from pages.components.header.locators import HeaderLocators

class HeaderComponent():

    def __init__(self, page: Page):
        self.page = page

    def open_menu(self):
        with allure.step('Открыть боковое меню'):
            self.page.locator(HeaderLocators.OPEN_MENU_BTN).click()

    def logout_btn_click(self):
        with allure.step('Нажать кнопку logout'):
            self.page.locator(HeaderLocators.LOGOUT_BTN).click()

    def check_url(self):
        with allure.step('url страницы должен быть https://www.saucedemo.com/'):
            expect(self.page).to_have_url('https://www.saucedemo.com/')

    def logout_full_path(self):
        with allure.step('Разлогиниться'):
            self.open_menu()
            self.logout_btn_click()
            self.check_url()