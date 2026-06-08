import pytest
from playwright.sync_api import Page

from pages.main_page.main_page import MainPage
from pages.authenication_page.authentication_page import AuthenticationPage
from pages.private_cabinet_page.private_cabinet_page import PrivateCabinetPage

"""
Фикстуры создающие экземпляры классов соответствующих страниц для использования при построении тестов. 
"""


@pytest.fixture(scope='function')
def main_page(page: Page) -> MainPage:
    return MainPage(page=page)


@pytest.fixture(scope='function')
def authentication_page(page: Page) -> AuthenticationPage:
    return AuthenticationPage(page=page)


@pytest.fixture(scope='function')
def private_cabinet_page(page: Page) -> PrivateCabinetPage:
    return PrivateCabinetPage(page=page)
