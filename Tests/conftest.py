import pytest
from selenium import webdriver
from time import sleep
from Config.config import TestData

@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_PATHE)
    if request.param == "firefox":
        web_driver = webdriver.Chrome(executable_path=TestData.firefox)

    request.cls.driver = web_driver
    request.cls.driver.get(TestData.BASE_URL)
    #web_driver.implicitly_wait(15)
    yield
    sleep(9.0)
    web_driver.close()
