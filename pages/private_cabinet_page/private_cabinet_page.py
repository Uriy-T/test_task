from playwright.sync_api import Page

from page_elements.button import Button
from page_elements.label import Label
from pages.base_page import BasePage
from pages.private_cabinet_page.private_cabinet_locators import PrivateCabinetLocators


class PrivateCabinetPage(BasePage):
    """
    Класс страницы личного кабинета.
    """

    def __init__(self, page: Page):
        super().__init__(page)

        self.avatar_menu_button = Button(page, PrivateCabinetLocators.AVATAR_MENU, name='avatar_menu_button')
        self.open_profile_button = Button(page, PrivateCabinetLocators.OPEN_PRIVATE_CABINET, name='open_profile_button')
        self.author_name = Label(page, PrivateCabinetLocators.AUTHOR_NAME, name='author_name')
        self.avatar = Label(page, PrivateCabinetLocators.AVATAR, name='avatar')

        self.exit_button = Button(page, PrivateCabinetLocators.EXIT_BUTTON, name="exit_button")

    def navigate_to_profile_page(self):
        self.avatar_menu_button.move_cursor_to_element()
        self.open_profile_button.click()

    def check_visible(self):
        self.author_name.check_visible()
        self.avatar.check_visible()

    def check_element_to_have_text(self):
        self.author_name.check_have_text('summer_writer')

    def exit_from_private_cabinet(self):
        self.avatar_menu_button.move_cursor_to_element()
        self.exit_button.click()
