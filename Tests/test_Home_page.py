from time import sleep

import pytest
from Tests.test_basePage import BaseTest
from Pages.HomePage import HomePage
from Config.config import TestData
from Pages.BasePage import BasePage


class Test_HomePage(BaseTest):
    @pytest.mark.Go
    def test_check_titlePage(self):
        self.homePage = HomePage(self.driver)
        # sleep(3.0)
        result = self.homePage.get_title(self.homePage.TITLE)
        print("\n", result)
        assert result == self.homePage.TITLE,"The title not match to: " + str(self.homePage.TITLE)

    @pytest.mark.Go
    def test_check_clickButton_Go(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_clickOnButton()

    def test_drop_down(self):
        self.homePage = HomePage(self.driver)
        # self.homePage.click_on_dropDwon()
        self.homePage.aa()