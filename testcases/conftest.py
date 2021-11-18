from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

@pytest.fixture()
def SetUp():
    driver=webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver')
    return driver

@pytest.fixture()
def HeadlessMode():
    chrome_options=Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver',chrome_options=chrome_options)
    return driver



# def pytest_configure(config):
#     config._metadata['Project Name']='Ecommerce WebPage Testing'
#     config._metadata['Modeule Name']='Customer UserTesting'
#     config._metadata['Tester']='Bharani'
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("Plugins",None)


