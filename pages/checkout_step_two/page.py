import allure

from playwright.sync_api import expect

from pages.base.page import BasePage
from pages.checkout_step_two.locators import CheckoutStepTwoLocators

class CheckoutStepTwoPage(BasePage):

    def get_item_name(self, item):
        with allure.step('Получить название элемента со страницы корзины'):
            return item.locator(CheckoutStepTwoLocators.INVENTORY_ITEM_NAME)

    def get_item_desc(self, item):
        with allure.step('Получить описание элемента со страницы корзины'):
            return item.locator(CheckoutStepTwoLocators.INVENTORY_ITEM_DESC)

    def get_item_price(self, item):
        with allure.step('Получить цену элемента со страницы корзины'):
            return item.locator(CheckoutStepTwoLocators.INVENTORY_ITEM_PRICE)

    def get_item_info(self):
        with allure.step('Получить данные элемента со страницы корзины'):
            item_data_from_cart = {
                'item_name': self.get_item_name,
                'item_desc': self.get_item_desc,
                'item_price': self.get_item_price

            }

            return item_data_from_cart

    def finish_btn_click(self):
        with allure.step('Нажать кнпоку Finish'):
            self.page.locator(CheckoutStepTwoLocators.FINISH_BTN).click()

    def get_count_items(self):
        with allure.step('Получить количество элементов на странице корзины'):
            return self.page.locator(CheckoutStepTwoLocators.INVENTORY_ITEM)

    def get_item(self, index):
        with allure.step(f'Получить элемент с индексом {index}'):
            return self.page.locator(CheckoutStepTwoLocators.INVENTORY_ITEM).nth(index)

    def check_total_price(self):
        with (allure.step('Проверить соответствие отображаемой суммы всех товаров')):
            i = int(self.get_count_items().count()) - 1
            total_price = 0
            while i >= 0:
                total_price += float(self.get_item(i).locator(CheckoutStepTwoLocators.INVENTORY_ITEM_PRICE
                                                        ).inner_text().replace('$', ''))
                i -= 1
            expect(CheckoutStepTwoLocators.SUBTOTAL_PRICE).to_have_text(f'Item total: {total_price}')
