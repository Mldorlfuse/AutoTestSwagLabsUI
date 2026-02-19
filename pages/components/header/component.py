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

    def logout_full_path(self):
        with allure.step('Разлогиниться'):
            self.open_menu()
            self.logout_btn_click()

    def check_count(self, count):
        with allure.step(f'Возле иконки корзины должно быть число {count}'):
            if count == 0 :
                expect(self.page.locator(HeaderLocators.SHOPPING_CART_COUNT)).not_to_be_attached()
            else:
                expect(self.page.locator(HeaderLocators.SHOPPING_CART_COUNT)).to_have_text(count)

    def open_shopping_cart(self):
        with allure.step('Открыть меню корзины'):
            self.page.locator(HeaderLocators.OPEN_SHOPPING_CART_BTN).click()