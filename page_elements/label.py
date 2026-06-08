from page_elements.base_element import BaseElement


class Label(BaseElement):

    @property
    def type_of(self) -> str:
        return 'label'
