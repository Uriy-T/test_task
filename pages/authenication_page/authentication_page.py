import allure
from playwright.sync_api import Page

from pages.authenication_page.auth_locators import AuthLocators
from pages.base_page import BasePage
from page_elements.label import Label
from page_elements.one_line_input import OneLineInput
from page_elements.button import Button


class AuthenticationPage(BasePage):
    """
    Класс страницы Аутентификации. В этом приложении представлена в виде pop-up элемента.
    """

    def __init__(self, page: Page):
        super().__init__(page)

        self.user_email_input = OneLineInput(page, AuthLocators.EMAIL_INPUT, name='username')
        self.password_input = OneLineInput(page, AuthLocators.PASSWORD_INPUT, name='password')
        self.enter_button = Button(page, AuthLocators.ENTER_ACCOUNT_BUTTON, name='enter_button')
        self.wrong_email_or_pass_message = Label(page, AuthLocators.WRONG_EMAIL_OR_PASS, name='wrong data input')
        self.email_unfilled_message = Label(page, AuthLocators.EMAIL_FIELD_MUST_BE_FILLED,
                                            name='email_unfilled_message')
        self.pass_unfilled_message = Label(page, AuthLocators.PASS_FIELD_MUST_BE_FILLED, name='pass_unfilled_message')

    @allure.step('Проверяем, что поля формы видны')
    def check_visible(self):
        self.user_email_input.check_visible()
        self.password_input.check_visible()

    @allure.step('Заполняем поля формы данными')
    def fill_data(self, username: str, password: str):
        self.user_email_input.fill(username)
        self.password_input.fill(password)

    @allure.step('Проверяем, что введенные данные верно отображаются в полях')
    def check_data(self, username: str, password: str):
        self.user_email_input.check_have_value(username)
        self.password_input.check_have_value(password)

    @allure.step('Нажимаем на кнопку входа в систему')
    def click_enter_button(self):
        self.enter_button.click()

    @allure.step('Проверяем, что сообщение валидации присутствует и содержит ожидаемый текст')
    def check_validation_message(self, user_email: str = None, password: str = None):
        if user_email and password:
            self.wrong_email_or_pass_message.check_visible()
            self.wrong_email_or_pass_message.check_have_text('Неверный логин или пароль.')
        elif not user_email and password:
            self.email_unfilled_message.check_visible()
            self.email_unfilled_message.check_have_text('Необходимо заполнить это поле.')
        elif user_email and not password:
            self.pass_unfilled_message.check_visible()
            self.pass_unfilled_message.check_have_text('Необходимо заполнить это поле.')
        elif not user_email and not password:
            self.email_unfilled_message.check_visible()
            self.email_unfilled_message.check_have_text('Необходимо заполнить это поле.')
            self.pass_unfilled_message.check_visible()
            self.pass_unfilled_message.check_have_text('Необходимо заполнить это поле.')
