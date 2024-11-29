import allure
from base.base_page import BasePage
from data.links import Links


class RequestPage(BasePage):

    _PAGE_URL = Links.REQUEST_PAGE

    _SERVICES_TAB = "//sidenav//a[.//div[text()='Услуги']]"
    _NEW_REQUEST_BUTTON = "//app-layout-navbar//a[@href='/requests/new']"

    @allure.step("Click on the services tab")
    def click_on_services_tab(self):
        services_tab = self.wait.until(self.EC.element_to_be_clickable(self._SERVICES_TAB))
        services_tab.click()

    @allure.step("Click on the new request button")
    def click_on_new_request_button(self):
        button = self.wait.until(self.EC.element_to_be_clickable(self._NEW_REQUEST_BUTTON))
        button.click()
