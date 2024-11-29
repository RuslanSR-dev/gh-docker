import os
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


def options_chr():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--window-size=1900,1030")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-cache")
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    driver = webdriver.Chrome(options=chrome_options)
    return driver


# def options_fir():
#     firefox_options = webdriver.FirefoxOptions()
#     firefox_options.add_argument("--window-size=1900,1030")
#     # chrome_options.add_argument("--headless")
#     firefox_options.add_argument(
#         "--user-agent=Mozilla/5.0 (Windows NT 10.0) "
#         "AppleWebKit/537.36 (KHTML, like Gecko) "
#         "Chrome/124.0.0.0 Safari/537.36")
#     firefox_options.add_argument("--disable-blink-features=AutomationControlled")
#     driver = webdriver.Firefox(options=firefox_options)
#     return driver


@pytest.fixture(autouse=True)
def driver(request):
    driver = options_chr()  # if os.environ["BROWSER"] == "chrome" else options_fir()
    request.cls.driver = driver
    yield
    allure.attach(
        body=driver.get_screenshot_as_png(),
        name="Screenshot",
        attachment_type=AttachmentType.PNG
    )
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def take_screenshot_on_failure(request, driver):
    yield
    if request.node.rep_call.failed:
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name="Screen on failure",
            attachment_type=allure.attachment_type.PNG
        )

# @pytest.fixture(autouse=True, scope="session")
# def setup_environments_properties():
#     properties = {
#         "Stage": os.environ['STAGE'],
#         "Browser": os.environ['BROWSER'],
#         "Python_version": "3.12.5"
#     }
#     with open("allure-results/environment.properties", "w") as file:
#         for key, value in properties.items():
#             file.write(f"{key}={value}\n")
