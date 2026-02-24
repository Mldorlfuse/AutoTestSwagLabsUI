import pytest
from playwright.sync_api import sync_playwright

from pages.app import App

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture
def app(page):
    return App(page)