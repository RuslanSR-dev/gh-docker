import allure

from base.base_page import BasePage
from data.links import Links


class NewServicePage(BasePage):

    _PAGE_URL = Links.NEW_SERVICES_PAGE

    _NAME_FIELD = "//form//input[@name='name']"
    _SERVICE_CODE_FIELD = "//form//input[@name='number']"
    _TARIFF_FIELD = "//form//input[@name='rate']"
    _INTEGRA_CODE_FIELD = "//form//input[@name='serviceCode']"
    _REQUEST_TYPE_FIELD = "//form//kendo-multiselect[@name='requestTypeIds']"
    _REQUEST_TYPE_INPUT_FIELD = "//form//kendo-multiselect[@name='requestTypeIds']//input"
    _DESCRIPTION_FIELD = "//form//input[@name='description']"
    _BUTTON_SAVE = "//button[not(contains(@class, 'w-100 cursor-pointer')) and .//span[contains(., 'Сохранить')]]"
    _LOADER_BUTTON = "//button[not(contains(@class, 'w-100 cursor-pointer')) and .//span[contains(., 'Сохранить')]]//div[@role='progressbar']"

    @allure.step("Enter name")
    def enter_name(self, name):
        name_field = self.wait.until(self.EC.visibility_of_element_located(self._NAME_FIELD))
        name_field.send_keys(name)
        assert name_field.get_attribute("value") == name, "name incorrect"

    @allure.step("Enter service code")
    def enter_service_code(self, service_code):
        service_code_field = self.wait.until(self.EC.visibility_of_element_located(self._SERVICE_CODE_FIELD))
        service_code_field.send_keys(service_code)
        assert service_code_field.get_attribute("value") == service_code, "service_code incorrect"

    @allure.step("Enter tariff")
    def enter_tariff(self, tariff):
        tariff_field = self.wait.until(self.EC.visibility_of_element_located(self._TARIFF_FIELD))
        tariff_field.send_keys(tariff)
        assert tariff_field.get_attribute("value") == tariff, "tariff incorrect"

    @allure.step("Enter integra code")
    def enter_integra_code(self, integra_code):
        integra_code_field = self.wait.until(self.EC.visibility_of_element_located(self._INTEGRA_CODE_FIELD))
        integra_code_field.send_keys(integra_code)
        assert integra_code_field.get_attribute("value") == integra_code, "integra_code incorrect"

    @allure.step("Click on field and enter request type")
    def click_on_field_and_enter_request_type(self, request_type):
        request_type_field = self.wait.until(self.EC.element_to_be_clickable(self._REQUEST_TYPE_FIELD))
        request_type_field.click()

        request_type_input_field = self.wait.until(
            self.EC.visibility_of_element_located(self._REQUEST_TYPE_INPUT_FIELD))
        request_type_input_field.send_keys(request_type)
        request_type_input_field.send_keys(self.Keys.ENTER)
        assert request_type_field.text == request_type, "request_type incorrect"

    @allure.step("Enter description")
    def enter_description(self, description):
        description_field = self.wait.until(self.EC.visibility_of_element_located(self._DESCRIPTION_FIELD))
        description_field.send_keys(description)
        assert description_field.get_attribute("value") == description, "integra_code incorrect"

    @allure.step("Click on button Save")
    def click_on_button_save(self):
        button_save = self.wait.until(self.EC.element_to_be_clickable(self._BUTTON_SAVE))
        button_save.click()

    @allure.step("Check loder on the button is invisible")
    def check_loader_button(self):
        self.wait.until(self.EC.invisibility_of_element_located(self._LOADER_BUTTON))
