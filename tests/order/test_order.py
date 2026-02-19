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
    app.header_component.check_count(str(len(get_random_count)))
    app.cart_page.compare_count_in_cart_and_random(str(len(get_random_count)))
    app.cart_page.delete_from_cart()
    app.header_component.check_count(0)

@allure.epic("UI")
@allure.feature("Добавление и удаление из корзины")
@allure.story("Оформление товара")
def test_order_full_path(open_base_page_and_authorization, get_random_count, get_random_inform_data, app):
    app.inventory_page.add_random_items_to_cart(get_random_count)
    app.header_component.open_shopping_cart()
    app.cart_page.check_out_btn_click()
    app.checkout_step_one.fill_all_and_submit(get_random_inform_data)

