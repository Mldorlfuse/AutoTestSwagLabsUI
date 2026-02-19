import allure

from playwright.sync_api import expect

from pages.base.page import BasePage
from pages.checkout_step_one.locators import CheckoutStepOneLocators

class CheckoutStepOnePage(BasePage):

    def fill_first_name(self, data):
        with allure.step(f'Заполнить поле имя значением {data}'):
            self.page.locator(CheckoutStepOneLocators.FIRST_NAME_INPUT).fill(data)

    def fill_last_name(self, data):
        with allure.step(f'Заполнить поле фамилия значением {data}'):
            self.page.locator(CheckoutStepOneLocators.LAST_NAME_INPUT).fill(data)

    def fill_postcode_name(self, data):
        with allure.step(f'Заполнить поле посткод значением {data}'):
            self.page.locator(CheckoutStepOneLocators.POSTAL_CODE_INPUT).fill(data)

    def click_continue_btn(self):
        with allure.step('Нажать кнопку Continue'):
            self.page.locator(CheckoutStepOneLocators.CONTINUE_BTN).click()

    def fill_all_and_submit(self, data):
        with allure.step(f'Заполнить поле формы Your Information и продолжить'):
            self.fill_first_name(data['first_name'])
            self.fill_last_name(data['last_name'])
            self.fill_postcode_name(data['postal_code'])
            self.click_continue_btn()


