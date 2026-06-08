from playwright.sync_api import Locator, expect

from page_elements.base_element import BaseElement


class OneLineInput(BaseElement):

    @property
    def type_of(self) -> str:
        return 'one_line_input'

    def fill(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_value(value)
