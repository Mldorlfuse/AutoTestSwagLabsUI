from test_data.auth.login import CorrectLoginData

import pytest

@pytest.fixture()
def open_base_page(base_page):
    base_page.open_base_page()

@pytest.fixture()
def authorization(login_page):
    login_page.login(CorrectLoginData)