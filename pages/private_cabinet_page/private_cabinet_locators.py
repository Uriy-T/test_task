from enum import StrEnum


class PrivateCabinetLocators(StrEnum):
    AVATAR_MENU = '//div[@class="avatar default-avatar"]'
    OPEN_PRIVATE_CABINET = '//a[@class="link-with-icon"]/i[@class="icon-user"]'
    AUTHOR_NAME = '//a[contains(., "summer_writer")]'
    AVATAR = '//div[@class=" default-avatar"]'

    EXIT_BUTTON = '//i[@class="icon-exit"]'