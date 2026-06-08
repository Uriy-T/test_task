from playwright.sync_api import Page

from page_elements.button import Button
from page_elements.label import Label
from pages.base_page import BasePage
from pages.main_page.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """
    Класс главной страницы приложения.
    """

    def __init__(self, page: Page):
        super().__init__(page)

        self.popular_books = Label(page, MainPageLocators.POPULAR_PUBLICATIONS, name='POPULAR_PUBLICATIONS')
        self.hot_news = Label(page, MainPageLocators.HOT_NEWS, name='HOT_NEWS')
        self.enter_menu_button = Button(page, MainPageLocators.ENTER_MENU_BUTTON, name='enter_button')

    def check_visible_publication_blocks(self):
        self.popular_books.check_visible()
        self.hot_news.check_visible()

    def check_visible_enter_menu_button(self):
        self.enter_menu_button.check_visible()

    def check_publication_blocks_to_have_text(self):
        self.popular_books.check_have_text('Популярное')
        self.hot_news.check_have_text('Горячие новинки')
        self.enter_menu_button.check_have_text('Войти')

    def navigate_to_authorization_page(self):
        self.enter_menu_button.click()
