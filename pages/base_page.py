from typing import Pattern
import allure
from playwright.sync_api import Page, expect


class BasePage:
    """
    Класс базовой страницы. Содержит действия, общие для всех страниц.
    Конструктор класса принимает объект типа Page (Playwright)
    """

    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        descr = f'Открываем страницу с адресом: {url}'

        with allure.step(descr):
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        descr = f'Перезагружаем страницу с адресом: {self.page.url}'

        with allure.step(descr):
            self.page.reload(wait_until='networkidle')

    def check_current_url(self, expected_url: Pattern[str] | str):
        descr = f'Проверяем, что открыта страница с верным адресом: {self.page.url}'

        with allure.step(descr):
            expect(self.page).to_have_url(expected_url)
