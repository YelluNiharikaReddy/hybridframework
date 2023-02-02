import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup():
        s = Service("C:\\Users\Dell\Desktop\chrome driver\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        print("launching chrome browser.............")
        return driver


# pytest HTML Reports


def pytest_configure(config):
    config._metadata['project Name'] = 'nopcommerce'
    config._metadata['module Name'] = 'customer'
    config._metadata['Tester'] = 'Niharika'

### it is hook for delete/modify environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_home", None)
    metadata.pop("plugins", None)
