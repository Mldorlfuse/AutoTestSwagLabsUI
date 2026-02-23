import random

import allure

from playwright.sync_api import expect

from pages.base.page import BasePage
from pages.checkout_step_two.locators import CheckoutStepTwoLocators

class CheckoutStepTwoPage(BasePage):

    def get_item_name(self, item):
        with allure.step('Получить название элемента со страницы проверки'):
            return item.locator(CheckoutStepTwoLocators.INVENTORY_ITEM_NAME).text_content()

    def get_item_desc(self, item):
        with allure.step('Получить описание элемента со страницы проверки'):
            return item.locator(CheckoutStepTwoLocators.INVENTORY_ITEM_DESC).text_content()

    def get_item_price(self, item):
        with allure.step('Получить цену элемента со страницы проверки'):
            return item.locator(CheckoutStepTwoLocators.INVENTORY_ITEM_PRICE).text_content()

    def get_item_info(self, item):
        with allure.step('Получить данные элемента со страницы проверки'):
            item_data= {
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

    def finish_btn_click(self):
        with allure.step('Нажать кнпоку Finish'):
            self.page.locator(CheckoutStepTwoLocators.FINISH_BTN).click()

    def get_count_items(self):
        with allure.step('Получить количество элементов на странице корзины'):
            return self.page.locator(CheckoutStepTwoLocators.INVENTORY_ITEM)

    def get_item(self, index):
        with allure.step(f'Получить элемент с индексом {index}'):
            return self.page.locator(CheckoutStepTwoLocators.INVENTORY_ITEM).nth(index)

    total_price = 0

    def check_total_price(self):
        with (allure.step('Проверить соответствие отображаемой суммы всех товаров')):
            i = int(self.get_count_items().count()) - 1
            while i >= 0:
                self.total_price += float(self.get_item(i).locator(CheckoutStepTwoLocators.INVENTORY_ITEM_PRICE
                                                        ).inner_text().replace('$', ''))
                i -= 1

            expect(self.page.locator(CheckoutStepTwoLocators.SUBTOTAL_PRICE)).to_have_text(
                f'Item total: ${self.total_price}')

    final_price = 0

    def check_final_price(self):
        with allure.step('Проверить финальную стоимость'):
            self.final_price = float(self.page.locator(CheckoutStepTwoLocators.TAX_PRICE
                                                       ).inner_text().replace('Tax: $', '')) + self.total_price
            expect(self.page.locator(CheckoutStepTwoLocators.TOTAL_PRICE)).to_have_text(
                f'Total: ${self.final_price}')

    def check_all_price(self):
        with allure.step('Проверка соответствия цен'):
            self.check_total_price()
            self.check_final_price()

    index = ''

    def get_random_index(self):
        with allure.step('Получить случайный index'):
            if self.index == '':
                self.index = random.randint(0, int(self.get_count_items().count()) - 1)
                return self.index
            else:
                return self.index

    def click_on_item(self, index):
        with allure.step('Перейти на страницу случайного элемента'):
            self.get_item(index).locator(CheckoutStepTwoLocators.INVENTORY_ITEM_NAME).click()