import allure

from playwright.sync_api import expect

from pages.base.page import BasePage
from pages.cart.locators import CartLocators

class CartPage(BasePage):

    def get_item_name(self, item):
        with allure.step('Получить название элемента со страницы корзины'):
            return item.locator(CartLocators.INVENTORY_ITEM_NAME)

    def get_item_desc(self, item):
        with allure.step('Получить описание элемента со страницы корзины'):
            return item.locator(CartLocators.INVENTORY_ITEM_DESC)

    def get_item_price(self, item):
        with allure.step('Получить цену элемента со страницы корзины'):
            return item.locator(CartLocators.INVENTORY_ITEM_PRICE)

    def get_item_info(self):
        with allure.step('Получить данные элемента со страницы корзины'):
            item_data_from_cart = {
                'item_name': self.get_item_name,
                'item_desc': self.get_item_desc,
                'item_price': self.get_item_price

            }

            return item_data_from_cart

    def get_count_items(self):
        with allure.step('Получить количество элементов на странице корзины'):
            return self.page.locator(CartLocators.INVENTORY_ITEM)

    def get_item(self, index):
        with allure.step(f'Получить элемент с индексом {index}'):
            return self.page.locator(CartLocators.INVENTORY_ITEM).nth(index)

    def compare_count_in_cart_and_random(self, count):
        with allure.step(f'сравнить количество элементов на странице корзины с количеством добавленных'):
            expect(self.get_count_items()).to_have_count(int(count))

    def delete_from_cart(self):
        with allure.step('Удалить элементы на странице корзины'):
            i = int(self.get_count_items().count()) - 1
            while i >= 0:
                self.get_item(i).locator(CartLocators.INVENTORY_ITEM_REMOVE_BTN).click()
                i -= 1

    def check_out_btn_click(self):
        with allure.step('Нажать кнопку Checkout'):
            self.page.locator(CartLocators.CHECKOUT_BTN).click()
