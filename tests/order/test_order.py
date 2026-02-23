import pytest
import allure

@allure.epic("UI")
@allure.feature("Добавление и удаление из корзины")
@allure.story("Добавление в корзину случайного количества элементов")
def test_add_to_cart_random_count(open_base_page_and_authorization, get_random_count, app):
    app.inventory_page.add_random_items_to_cart(get_random_count)
    app.header_component.check_count(str(len(get_random_count)))
    app.inventory_page.remove_random_items_from_cart(get_random_count)
    app.header_component.check_count(0)

@allure.epic("UI")
@allure.feature("Добавление и удаление из корзины")
@allure.story("Добавление элементов в корзину и удаление их на странице корзины")
def test_add_to_cart_random_count_and_remove(open_base_page_and_authorization, get_random_count, app):
    app.inventory_page.add_random_items_to_cart(get_random_count)
    app.header_component.open_shopping_cart()
    app.cart_page.delete_from_cart()
    app.header_component.check_count(0)

@allure.epic("UI")
@allure.feature("Оформление товара")
@allure.story("Оформление товара")
def test_order_full_path(open_base_page_and_authorization, get_random_count, get_random_inform_data, app):
    app.inventory_page.add_random_items_to_cart(get_random_count)
    app.header_component.open_shopping_cart()
    app.cart_page.checkout_btn_click()
    app.checkout_step_one.fill_all_and_submit(get_random_inform_data)
    app.checkout_step_two.finish_btn_click()
    app.checkout_complete.check_all_text_and_click_back_home()
    app.base_page.check_url('https://www.saucedemo.com/inventory.html')

@allure.epic("UI")
@allure.feature("Оформление товара")
@allure.story("Проверка соответствия информации отображаемой на каждой странице этапа оформления товара")
def test_check_all_information_at_all_pages(
        open_base_page_and_authorization, get_random_count, get_random_inform_data, app):

    list_items_from_main_page = []
    list_items_from_cart_page = []
    list_items_from_checkout_page = []
    random_item_from_checkout_page = {}
    item_form_inventory_item_page = {}

    app.inventory_page.add_random_items_to_cart(get_random_count)
    list_items_from_main_page = app.inventory_page.create_list_items_info(get_random_count)

    app.header_component.open_shopping_cart()
    list_items_from_cart_page = app.cart_page.create_list_items_info()

    app.base_page.check_the_match_of_these_elements(list_items_from_main_page, list_items_from_cart_page)
    app.cart_page.checkout_btn_click()
    app.checkout_step_one.fill_all_and_submit(get_random_inform_data)
    list_items_from_checkout_page = app.checkout_step_two.create_list_items_info()

    app.checkout_step_two.check_all_price()

    app.base_page.check_the_match_of_these_elements(list_items_from_main_page, list_items_from_checkout_page)
    random_item_from_checkout_page = app.checkout_step_two.get_item_info(
        app.checkout_step_two.get_item(app.checkout_step_two.get_random_index())
    )
    app.checkout_step_two.click_on_item(app.checkout_step_two.get_random_index())

    item_form_inventory_item_page = app.inventory_item_page.get_item_info()
    app.base_page.check_the_match_of_these_elements(random_item_from_checkout_page, item_form_inventory_item_page)
