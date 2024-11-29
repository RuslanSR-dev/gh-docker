import os
import allure
from base.base_page import BasePage
from data.links import Links


class LoginPage(BasePage):

    _PAGE_URL = Links.LOGIN_PAGE

    _LOGIN_FIELD = "//input[@id='login']"
    _PASSWORD_FIELD = "//input[@id='password']"
    _LOGIN_BUTTON = "//button[not(contains(@class, 'w-100 cursor-pointer'))]"

    @allure.step("Enter login")
    def enter_login(self, login):
        login_field = self.wait.until(self.EC.visibility_of_element_located(self._LOGIN_FIELD))
        login_field.send_keys(login)
        assert login_field.get_attribute("value") == login, "login incorrect"

    @allure.step("Enter password")
    def enter_password(self, password):
        password_field = self.wait.until(self.EC.visibility_of_element_located(self._PASSWORD_FIELD))
        password_field.send_keys(password)
        assert password_field.get_attribute("value") == password, "password incorrect"

    @allure.step("Click on button login")
    def click_on_button_login(self):
        button = self.wait.until(self.EC.element_to_be_clickable(self._LOGIN_BUTTON))
        button.click()

    @allure.step("Account login")
    def login(self, login, password):
        self.enter_login(login)
        self.enter_password(password)
        self.click_on_button_login()