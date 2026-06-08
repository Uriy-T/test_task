from enum import StrEnum


class MainPageLocators(StrEnum):
    POPULAR_PUBLICATIONS = '//h2[@class="section-title clearfix"]/a[@href = "/work/genre/all?sorting=popular"]'
    HOT_NEWS = '//h2[@class="section-title clearfix"]/a[@href = "/work/genre/all?pub=3&sorting=popular"]'
    ENTER_MENU_BUTTON = '//a[@onclick="app.showLoginModal();"]'

