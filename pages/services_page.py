import allure

from base.base_page import BasePage
from data.links import Links


class ServicesPage(BasePage):

    _PAGE_URL = Links.SERVICES_PAGE

    _BUTTON_NEW_SERVICES = "//button[contains(., 'Новая услуга')]"
    _BUTTON_BURGER = "//a[contains(@class, 'layout-sidenav-toggle')]"

    @allure.step("Click on the button new service")
    def click_on_button_new_service(self):
        button = self.wait.until(self.EC.element_to_be_clickable(self._BUTTON_BURGER))
        button.click()
        button_new_service = self.wait.until(self.EC.element_to_be_clickable(self._BUTTON_NEW_SERVICES))
        button_new_service.click()
