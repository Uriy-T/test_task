import pytest
import allure

from environmernts.environments_pages_url import PageURL
from pages.authenication_page.authentication_page import AuthenticationPage
from pages.main_page.main_page import MainPage
from pages.private_cabinet_page.private_cabinet_page import PrivateCabinetPage
from tools.allure.tags import ModuleForTesting, SeverityTest, TypeTest
from test_data.auth_datasets import valid_data_set, invalid_dataset
from tools.data_tools.input_data_formater import input_data_formater
from tools.allure.hierarchy_tests import System, FunctionalityModule, Suite


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(ModuleForTesting.AUTHORIZATION)
@allure.parent_suite(System.TASK_MANAGER)
@allure.suite(FunctionalityModule.AUTHORIZATION)
@allure.sub_suite(Suite.BASE_VALIDATION)
class TestAuthentication:

    @allure.title('Тест авторизации с невалидными данными')
    @allure.tag(TypeTest.NEGATIVE)
    @allure.severity(SeverityTest.BLOCKER)
    @pytest.mark.parametrize(*input_data_formater(invalid_dataset))
    def test_authorization_negative(self,
                                    main_page: MainPage,
                                    authentication_page: AuthenticationPage,
                                    user_email: str,
                                    password: str):
        main_page.visit(PageURL.MAIN_PAGE)
        main_page.check_visible_publication_blocks()
        main_page.check_publication_blocks_to_have_text()
        main_page.navigate_to_authorization_page()

        authentication_page.check_current_url(PageURL.AUTH_Page)
        authentication_page.check_visible()
        authentication_page.fill_data(username=user_email, password=password)
        authentication_page.check_data(username=user_email, password=password)
        authentication_page.click_enter_button()
        authentication_page.check_validation_message(user_email=user_email, password=password)

    @allure.title('Тест авторизации с валидными данными')
    @allure.tag(TypeTest.POSITIVE)
    @allure.severity(SeverityTest.BLOCKER)
    @pytest.mark.parametrize(*input_data_formater(valid_data_set))
    def test_successful_authentication(self,
                                       main_page: MainPage,
                                       authentication_page: AuthenticationPage,
                                       private_cabinet_page: PrivateCabinetPage,
                                       user_email: str,
                                       password: str):
        main_page.visit(PageURL.MAIN_PAGE)
        main_page.check_visible_publication_blocks()
        main_page.check_publication_blocks_to_have_text()
        main_page.navigate_to_authorization_page()

        authentication_page.check_current_url(PageURL.AUTH_Page)
        authentication_page.check_visible()
        authentication_page.fill_data(username=user_email, password=password)
        authentication_page.check_data(username=user_email, password=password)
        authentication_page.click_enter_button()

        private_cabinet_page.navigate_to_profile_page()
        private_cabinet_page.check_current_url(PageURL.PROFILE)
        private_cabinet_page.check_visible()
        private_cabinet_page.check_element_to_have_text()
        private_cabinet_page.exit_from_private_cabinet()

        main_page.check_current_url(PageURL.MAIN_PAGE)
        main_page.check_visible_publication_blocks()
        main_page.check_publication_blocks_to_have_text()