import allure
from playwright.sync_api import Page, Locator, expect


class BaseElement:
    """
    Класса базового элемента интерфейса web-страницы. Конструктор принимает на вход:
    - объект типа Page;
    - локатор элемента;
    - имя элемента для отслеживания в allure шагах
    Описывает общие действия, которые можно совершить с элементами web-страницы.
    """

    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    def type_of(self) -> str:
        return 'base element'

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.locator(locator).nth(nth)

    def check_visible(self, nth: int = 0, **kwargs):
        descr = f'Проверка видимости элемента {self.name} (тип: {self.type_of})'

        with allure.step(descr):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_visible()

    def check_enabled(self, nth: int = 0, **kwargs):
        descr = f'Проверка доступности взаимодействия с элементом {self.name} (тип: {self.type_of})'

        with allure.step(descr):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        descr = f'Проверка НЕдоступности взаимодействия с элементом {self.name} (тип: {self.type_of})'

        with allure.step(descr):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_disabled()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        descr = f'Проверка, что элемент {self.name} (тип: {self.type_of}) имеет в составе текст: "{text}"'

        with allure.step(descr):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_text(text)

    def move_cursor_to_element(self, nth: int = 0, **kwargs):
        descr = f'Наводим курсор на элемент {self.name} (тип: {self.type_of})'

        with allure.step(descr):
            locator = self.get_locator(nth, **kwargs)
            locator.hover()

    def click(self, nth: int = 0, **kwargs):
        descr = f'Клик по элементу {self.name} (тип: {self.type_of})'

        with allure.step(descr):
            locator = self.get_locator(nth, **kwargs)
            locator.click()

    def scroll_to_element(self, nth: int = 0, **kwargs):
        descr = f'Скролл страницы до элемента {self.name} (тип: {self.type_of})'

        with allure.step(descr):
            locator = self.get_locator(nth, **kwargs)
            locator.scroll_into_view_if_needed()
