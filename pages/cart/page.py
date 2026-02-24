import allure

from playwright.sync_api import expect

from pages.base.page import BasePage
from pages.cart.locators import CartLocators

class CartPage(BasePage):

    CartLocators = CartLocators

    def get_item_name(self, item):
        with allure.step('Получить название элемента со страницы корзины'):
            return item.locator(CartLocators.INVENTORY_ITEM_NAME).text_content()

    def get_item_desc(self, item):
        with allure.step('Получить описание элемента со страницы корзины'):
            return item.locator(CartLocators.INVENTORY_ITEM_DESC).text_content()

    def get_item_price(self, item):
        with allure.step('Получить цену элемента со страницы корзины'):
            return item.locator(CartLocators.INVENTORY_ITEM_PRICE).text_content()

    def get_item_info(self, item):
        with allure.step('Получить данные элемента со страницы корзины'):
            item_data = {
                'item_name': self.get_item_name(item),
                'item_desc': self.get_item_desc(item),
                'item_price': self.get_item_price(item)

            }

            return item_data

    def create_list_items_info(self):
        with allure.step('Добавить информацию об элементе в список'):
            list_items = []
            i = int(self.get_count_items().count()) - 1
            while i >= 0:
                list_items.append(self.get_item_info(self.get_item(i)))
                i -= 1
            return list_items

    def get_count_items(self):
        with allure.step('Получить количество элементов на странице корзины'):
            return self.page.locator(CartLocators.INVENTORY_ITEM)

    def get_item(self, index):
        with allure.step(f'Получить элемент с индексом {index}'):
            return self.page.locator(CartLocators.INVENTORY_ITEM).nth(index)

    def delete_from_cart(self):
        with allure.step('Удалить элементы на странице корзины'):
            i = int(self.get_count_items().count()) - 1
            while i >= 0:
                self.get_item(i).locator(CartLocators.INVENTORY_ITEM_REMOVE_BTN).click()
                i -= 1

    def checkout_btn_click(self):
        with allure.step('Нажать кнопку Checkout'):
            self.page.locator(CartLocators.CHECKOUT_BTN).click()
