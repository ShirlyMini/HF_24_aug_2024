import time

import pytest
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service as edge_service
from selenium.webdriver.firefox.service import Service as ff_service
from Utilities.ReadConfig import ReadProperty
@pytest.fixture()
def launch_browser(request):
    browser = request.config.getoption("--browser")
    if browser=="chrome":
        op=Options()
        op.add_argument("--headless")
        op.add_argument("--incognito")
        service_obj = chrome_service(ReadProperty.GetChomeDriver())
        driver = webdriver.Chrome(service=service_obj, options=op)
    elif browser=="edge":
        service_obj = edge_service(ReadProperty.GetEdgeDriver())
        driver = webdriver.Edge(service=service_obj)
    elif browser=="firefox" or browser=="ff":
        service_obj = ff_service(ReadProperty.GetFirefoxDriver())
        driver = webdriver.Firefox(service=service_obj)
    else:
        op = Options()
        op.add_argument("--auto-open-devtools-for-tabs")
        service_obj = chrome_service(ReadProperty.GetChomeDriver())
        driver = webdriver.Chrome(service=service_obj, options=op)

    driver.get(ReadProperty.GetUrl())
    driver.maximize_window()
    # time.sleep(30)
    driver.implicitly_wait(60)
    yield driver
    driver.quit()

def pytest_addoption(parser):  # this will get the values from CLI/hooks
    parser.addoption("--browser")


