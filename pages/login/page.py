import allure
from playwright.sync_api import Page, expect

from pages.base.page import BasePage

from pages.login.locators import LoginLocators

class LoginPage(BasePage):

    def fill_username(self, username):
        with allure.step(f'Ввести {username} в поле username'):
            self.page.locator(LoginLocators.USERNAME_INPUT).fill(username)

    def fill_password(self, password):
        with allure.step(f'Ввести {password} в поле password'):
            self.page.locator(LoginLocators.PASSWORD_INPUT).fill(password)

    def check_error_message(self, error_message):
        with allure.step(f'Сообщение об ошибке соответствует {error_message}'):
            expect(self.page.locator(LoginLocators.ERROR_MESSAGE)).to_have_text(error_message)

    def submit_form(self):
        with allure.step('Нажать кнопку Login'):
            self.page.locator(LoginLocators.LOGIN_BUTTON).click()

    def check_url(self):
        with allure.step('url страницы должен быть https://www.saucedemo.com/'):
            expect(self.page).to_have_url('https://www.saucedemo.com/')

    def login(self, user):
        with allure.step('Авторизация'):
            self.fill_username(user.username)
            self.fill_password(user.password)
            self.submit_form()
        with allure.step('Была переадресация на url https://www.saucedemo.com/inventory.html'):
            expect(self.page).to_have_url('https://www.saucedemo.com/inventory.html')

    def login_and_check_error_message(self, user):
        with allure.step('Авторизоваться и проверить сообщение об ошибке'):
            self.fill_username(user.username)
            self.fill_password(user.password)
            self.submit_form()
            self.check_error_message(user.error_message)
