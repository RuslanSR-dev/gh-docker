import os
import allure
import pytest
from allure_commons.types import Severity
from base.base_test import BaseTest


@allure.epic("Services")
@allure.story("New services")
class TestAddNewServices(BaseTest):

    @allure.title("Add new services")
    @allure.severity(Severity.MINOR)
    @pytest.mark.regression
    def test_add_new_services(self):
        self.login_page.open()
        self.login_page.enter_login(os.getenv("LOGIN_DOCKER"))
        self.login_page.enter_password(os.getenv("PASSWORD_DOCKER"))
        self.login_page.click_on_button_login()
        self.request_page.is_opened()
        self.request_page.click_on_services_tab()
        self.services_page.is_opened()
        self.services_page.click_on_button_new_service()
        self.new_service_page.is_opened()
        self.new_service_page.enter_name("Test service")
        self.new_service_page.enter_service_code("020200020")
        self.new_service_page.enter_tariff("Tariff")
        self.new_service_page.enter_integra_code("23443-fhkjk39485-4386hg")
        self.new_service_page.click_on_field_and_enter_request_type("Монтаж")
        self.new_service_page.enter_description("Description")
        self.new_service_page.click_on_button_save()
        self.new_service_page.check_loader_button()
        self.services_page.check_loader_page()
        self.services_page.check_alert_success_visible()
        self.services_page.click_on_alert_success()
        self.services_page.check_alert_success_invisible()
        self.services_page.is_opened()
        self.services_page.click_on_logout_button()
        self.login_page.is_opened()

    @allure.title("Account login")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.smoke
    def test_login(self):
        self.login_page.open()
        self.login_page.login(os.getenv("LOGIN_DOCKER"), os.getenv("PASSWORD_DOCKER"))
        self.request_page.is_opened()

    @allure.title("Create a new request")
    @allure.severity(Severity.TRIVIAL)
    @pytest.mark.smoke
    def test_create_new_request(self):
        self.login_page.open()
        self.login_page.login(os.getenv("LOGIN_DOCKER"), os.getenv("PASSWORD_DOCKER"))
        self.request_page.is_opened()
        self.request_page.click_on_new_request_button()
        self.request_new_page.is_opened()
        self.request_new_page.click_on_logout_button()
        self.request_new_page.click_on_assertion_button()
        self.login_page.is_opened()
