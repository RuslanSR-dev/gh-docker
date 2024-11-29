from utils.generators import Generators
from data.credentials import Credentials
from pages.login_page import LoginPage
from pages.request_page import RequestPage
from pages.services_page import ServicesPage
from pages.new_service_page import NewServicePage
from pages.request_new_page import RequestNewPage


class BaseTest:

    def setup_method(self):
        self.generators = Generators()
        self.creds = Credentials()
        self.login_page = LoginPage(self.driver)
        self.request_page = RequestPage(self.driver)
        self.request_new_page = RequestNewPage(self.driver)
        self.services_page = ServicesPage(self.driver)
        self.new_service_page = NewServicePage(self.driver)
