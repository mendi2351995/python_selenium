import pytest
from selenium import webdriver
from time import sleep
from Config.config import TestData
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

@pytest.fixture(params=["chrome","edg"],scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver = webdriver.firefox(executable_path=GeckoDriverManager.install())
    if request.param == "edg":
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    if request.param == "IE":
        web_driver = webdriver.Ie(IEDriverManager().install())

    request.cls.driver = web_driver
    request.cls.driver.get(TestData.BASE_URL)
    #web_driver.implicitly_wait(15)
    yield
    sleep(9.0)
    web_driver.close()
