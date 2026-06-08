from enum import StrEnum


class AuthLocators(StrEnum):
    EMAIL_INPUT = '#Login'
    PASSWORD_INPUT = '//input[@type="password"]'

    ENTER_ACCOUNT_BUTTON = '(//button[@class="btn btn-primary btn-block mt-lg"])[1]'
    WRONG_EMAIL_OR_PASS = '//li[contains(.,"Неверный логин или пароль.")]'
    EMAIL_FIELD_MUST_BE_FILLED = '//span[@data-bind="validationMessage: login"]'
    PASS_FIELD_MUST_BE_FILLED = '//span[@data-bind="validationMessage: password"]'