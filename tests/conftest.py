from test_data.auth.login import CorrectLoginData

import pytest
import random
from faker import Faker

fake = Faker()

@pytest.fixture()
def open_base_page(app):
    app.base_page.open_base_page()

@pytest.fixture()
def authorization(app):
    app.login_page.login(CorrectLoginData)

@pytest.fixture()
def open_base_page_and_authorization(app):
    app.base_page.open_base_page()
    app.login_page.login(CorrectLoginData)

@pytest.fixture(scope="session")
def get_random_count():
    return random.sample(range(0, 6), random.randint(1, 6))

@pytest.fixture(scope="session")
def get_random_inform_data():
    inform_data = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'postal_code': fake.postalcode()
    }
    return inform_data
