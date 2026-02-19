import allure
from playwright.sync_api import expect

from pages.base.page import BasePage

from pages.inventory.locators import InventoryLocators

class InventoryPage(BasePage):

    def get_item_name(self, item):
        with allure.step('Получить название элемента с главного экрана'):
            return item.locator(InventoryLocators.INVENTORY_ITEM_NAME)

    def get_item_desc(self, item):
        with allure.step('Получить описание элемента с главного экрана'):
            return item.locator(InventoryLocators.INVENTORY_ITEM_DESC)

    def get_item_price(self, item):
        with allure.step('Получить цену элемента с главного экрана'):
            return item.locator(InventoryLocators.INVENTORY_ITEM_PRICE)

    def get_item_info(self):
        with allure.step('Получить данные элемента с главного экрана'):
            item_data = {
                'item_name': self.get_item_name,
                'item_desc': self.get_item_desc,
                'item_price': self.get_item_price

            }

            return item_data

    def add_to_cart_by_index(self, index):
        with allure.step('Добавить элемент в корзину'):
            self.get_item(index).locator(InventoryLocators.INVENTORY_ITEM_ADD_TO_CART).click()

    def remove_from_cart_by_index(self, index):
        with allure.step('Удалить элемент из карзины'):
            self.get_item(index).locator(InventoryLocators.INVENTORY_ITEM_REMOVE_FROM_CART).click()

    def get_item(self, index):
        with allure.step(f'Получить элемент с индексом {index}'):
            return self.page.locator(InventoryLocators.INVENTORY_ITEM).nth(index)

    def add_random_items_to_cart(self, random_count):
        with allure.step('Добавить случайные элементы в корзину'):
            for number in random_count:
                self.add_to_cart_by_index(number)

    def remove_random_items_from_cart(self, random_count):
        with allure.step('Удалить случайные элементы из корзины'):
            for number in random_count:
                self.remove_from_cart_by_index(number)
