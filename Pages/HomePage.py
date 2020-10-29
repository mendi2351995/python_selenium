from Pages.BasePage import BasePage
from Config.config import TestData

from selenium.webdriver.common.by import By

class HomePage(BasePage):
    TITLE = "Super Calculator"
    BUTTON_GO = (By.ID,"gobutton")

    def __init__(self,driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)

    def get_HomePage_title(self,title):
        return self.get_title(title)

    def do_clickOnButton(self):
        self.do_click(self.BUTTON_GO)

    def click_on_element_with_wait(self):
        self.fluentWait_click(self.BUTTON_GO)
