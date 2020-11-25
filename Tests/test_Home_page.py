from time import sleep
import random
import pytest
import allure
from Tests.test_basePage import BaseTest
from Pages.HomePage import HomePage
from Config.config import TestData
from Pages.BasePage import BasePage

@allure.severity(allure.severity_level.NORMAL)
class Test_HomePage(BaseTest):
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.fixture
    def homePage(self):
    #pytest Tests/test_Home_page.py -v --junitxml="result.xml"
        return HomePage(self.driver)

    @pytest.mark.Go
    def test_check_titlePage(self,homePage):
        # sleep(3.0)
        result = homePage.get_title(homePage.TITLE)
        print("\n", result)
        assert result == homePage.TITLE,"The title not match to: " + str(homePage.TITLE)

    @pytest.mark.Go
    def test_check_clickButton_Go(self,homePage):
        homePage.do_clickOnButton()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.Go
    def test_drop_down(self,homePage):
        # self.homePage = HomePage(self.driver)
        # self.homePage.click_on_dropDwon()
        #homePage.select_on_one_element()
        homePage.screenshoth_to_reporta()

    @pytest.mark.flaky(reruns=2)
    def test_example(self):
        assert 1==2,ValueError
    