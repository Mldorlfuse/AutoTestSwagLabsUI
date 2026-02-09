import pytest
from playwright.sync_api import sync_playwright

from pages.login.page import BasePage
from pages.login.page import LoginPage
from pages.components.header.component import HeaderComponent

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture
def base_page(page):
    return BasePage(page)

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def header_component(page):
    return HeaderComponent(page)