import pytest
import allure

from test_data.auth.login import CorrectLoginData, LockedLoginData, WrongLoginData, WithoutPasswordData, WithoutLoginData

@allure.epic("UI")
@allure.feature("Авторизация")
@allure.story("Авторизация с корректными данными")
def test_login_with_correct_data(open_base_page, app):
    app.login_page.login(CorrectLoginData)

@allure.epic("UI")
@allure.feature("Авторизация")
@allure.story("Авторизация с некорректными данными")
@pytest.mark.parametrize('logins', [LockedLoginData, WrongLoginData, WithoutLoginData, WithoutPasswordData])
def test_login_with_incorrect_data(open_base_page, app, logins):
    app.login_page.login_and_check_error_message(logins)

@allure.epic("UI")
@allure.feature("Авторизация")
@allure.story("Авторизация и выход из аккаунта")
def test_login_and_logout(open_base_page_and_authorization, app):
    app.header_component.logout_full_path()
    app.login_page.check_url()