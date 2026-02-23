import allure

from playwright.sync_api import expect

from pages.base.page import BasePage
from pages.checkout_complete.locators import CheckoutCompleteLocators

class CheckoutCompletePage(BasePage):

    def check_title(self):
        with allure.step('Текст заголовка должен быть равен "Thank you for your order!"'):
            expect(self.page.locator(CheckoutCompleteLocators.COMPLETE_HEADER)).to_have_text(
                'Thank you for your order!')

    def check_text(self):
        with allure.step('''Текст подзаголовка должен быть равен 
                "Your order has been dispatched, and will arrive just as fast as the pony can get there!"'''):
            expect(self.page.locator(CheckoutCompleteLocators.COMPLETE_TEXT)).to_have_text(
                'Your order has been dispatched, and will arrive just as fast as the pony can get there!')

    def click_btn(self):
        with allure.step('Нажать кнопку Back home'):
            self.page.locator(CheckoutCompleteLocators.BACK_HOME_BTN).click()

    def check_all_text_and_click_back_home(self):
        with allure.step('Проверить весь текст и завершить заказ'):
            self.check_title()
            self.check_text()
            self.click_btn()

