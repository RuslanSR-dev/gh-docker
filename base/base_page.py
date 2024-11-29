import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.generators import Generators

from metaclasses.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):

    _LOGOUT_DROPDOWN = "//a[.//span[text()='Салахов Р. Р.']]"
    _LOGOUT_ITEM = "//a[contains(text(), 'Выход')]"
    _LOADER_PAGE = "//div[@kendogridloading]"
    _ALERT_SUCCESS = "//div[@id='toast-container'][.//div[@aria-label='Элемент создан успешно!']]"

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=3)
        self.generators = Generators()
        self.Keys = Keys
        self.EC = EC

    def open(self):
        with allure.step(f"Page open {self._PAGE_URL}"):
            self.driver.get(self._PAGE_URL)
            self.wait.until(self.EC.url_to_be(self._PAGE_URL))

    def is_opened(self):
        with allure.step(f"Page {self._PAGE_URL} is opened"):
            self.wait.until(self.EC.url_contains(self._PAGE_URL))

    @allure.step("Logout from account")
    def click_on_logout_button(self):
        self.wait.until(self.EC.element_to_be_clickable(self._LOGOUT_DROPDOWN)).click()
        self.wait.until(self.EC.element_to_be_clickable(self._LOGOUT_ITEM)).click()

    @allure.step("Check loader on the page is invisible")
    def check_loader_page(self):
        self.wait.until(self.EC.invisibility_of_element_located(self._LOADER_PAGE))

    @allure.step("Check alert success on the page is visible")
    def check_alert_success_visible(self):
        self.wait.until(self.EC.visibility_of_element_located(self._ALERT_SUCCESS))

    @allure.step("Click on the pop-up alert success")
    def click_on_alert_success(self):
        self.wait.until(self.EC.element_to_be_clickable(self._ALERT_SUCCESS)).click()

    @allure.step("Check alert success is invisible on the page")
    def check_alert_success_invisible(self):
        self.wait.until(self.EC.invisibility_of_element_located(self._ALERT_SUCCESS))
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG
        )
