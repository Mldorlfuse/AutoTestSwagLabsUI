import pytest

from test_data.auth.login import CorrectLoginData, LockedLoginData, WrongLoginData, WithoutPasswordData, WithoutLoginData

def test_login_with_correct_data(open_base_page, login_page):
    login_page.login(CorrectLoginData)

@pytest.mark.parametrize('logins', [LockedLoginData,WrongLoginData, WithoutLoginData, WithoutLoginData])
def test_login_with_incorrect_data(open_base_page, login_page, logins):
    login_page.login_and_check_error_message(logins)

def test_login_and_logout(open_base_page, authorization, header_component):
    header_component.logout_full_path()