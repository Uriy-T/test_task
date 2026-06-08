import pytest
from _pytest.fixtures import SubRequest
import allure
from playwright.sync_api import Playwright, Page
from config import settings, Browser


def start_browser(playwright: Playwright,
                  test_name: str,
                  browser_type: Browser
                  ) -> Page:
    """
    Базовая функция-генератор создающая для тестов объект страницы.
    :param playwright: встроенная фикстура pytest-playwright, используется вместо работы с контекстным менеджером with
    :param test_name: переменная принимающая имя теста для создания артефактов отслеживания тестов (видео, снэпшоты)
    :return: Возвращает объект тира Page.
    """
    browser = playwright[browser_type].launch(headless=settings.headless, args=['--start-maximized'])
    context = browser.new_context(no_viewport=True,
                                  record_video_dir='./videos',
                                  record_video_size={"width": 1920, "height": 1080})
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page

    context.tracing.stop(path=f'./tracing/{test_name}.zip')
    browser.close()

    allure.attach.file(source=f'./tracing/{test_name}.zip', name='trace', extension='zip')
    allure.attach.file(source=page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)


@pytest.fixture(scope='function', params=settings.browsers)
def page(request: SubRequest, playwright: Playwright) -> Page:
    """
    Общая фикстура, служащая для параметризации вызова генератора start_browser
    :param request: Объект класса SubRequest, позволяющий обращаться к параметрам тестов и использовать их.
    :param playwright: встроенная фикстура pytest-playwright, используется вместо работы с контекстным менеджером with
    :return: Возвращает объект тира Page.
    """
    yield from start_browser(playwright, test_name=request.node.name, browser_type=request.param)