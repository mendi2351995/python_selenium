from lib2to3.pgen2 import driver

from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Config.config import TestData
from time import sleep

from selenium.webdriver.common.by import By

class HomePage(BasePage):
    TITLE = "Super Calculator"
    BUTTON_GO = (By.ID,"gobutton")
    DROP_DWON = (By.XPATH,"//select[@ng-model='operator']")

    def __init__(self,driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)

    def get_HomePage_title(self,title):
        return self.get_title(title)

    def do_clickOnButton(self):
        self.do_click(self.BUTTON_GO)

    def click_on_dropDwon(self):
        List_DROP_DWON = self.driver.find_element_by_xpath("//select[@ng-model='operator']")
        self.multiselect_set_selections(List_DROP_DWON,"-")

    def click_on_element_with_wait(self):
        self.fluentWait_click(self.BUTTON_GO)

    def aa(self):
        element = self.driver.find_element(*self.DROP_DWON)
        self.multiselect_set_selections(element,"-")
        # selct = Select(element)
        # selct.deselect_by_visible_text('-')
