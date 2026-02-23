import allure

from playwright.sync_api import expect

from pages.base.page import BasePage
from pages.inventory_item.locators import InventoryItemLocators

class InventoryItemPage(BasePage):

    def get_item_name(self,):
        with allure.step('Получить название элемента со страницы элемента'):
            return self.page.locator(InventoryItemLocators.INVENTORY_ITEM_NAME).text_content()

    def get_item_desc(self):
        with allure.step('Получить описание элемента со страницы элемента'):
            return self.page.locator(InventoryItemLocators.INVENTORY_ITEM_DESC).text_content()

    def get_item_price(self):
        with allure.step('Получить цену элемента со страницы элемента'):
            return self.page.locator(InventoryItemLocators.INVENTORY_ITEM_PRICE).text_content()

    def get_item_info(self):
        with allure.step('Получить данные элемента со страницы элемента'):
            item_data = {
                'item_name': self.get_item_name(),
                'item_desc': self.get_item_desc(),
                'item_price': self.get_item_price()

            }

            return item_data