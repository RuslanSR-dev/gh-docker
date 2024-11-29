import allure
from base.base_page import BasePage
from data.links import Links


class RequestNewPage(BasePage):

    _PAGE_URL = Links.NEW_REQUEST_PAGE

    _ASSERTION_BUTTON = "//button[text()='Да, не сохранять изменения!']"

    @allure.step("Click on the assertion button")
    def click_on_assertion_button(self):
        button = self.wait.until(self.EC.element_to_be_clickable(self._ASSERTION_BUTTON))
        button.click()
