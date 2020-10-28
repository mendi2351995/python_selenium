from selenium.webdriver import ActionChains


'''imports stof for  function flouentWait: start'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
        '''end imports'''
class BasePage:
    def __init__(self,driver):
        self.driver = driver


    def do_click(self,by_locator):
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(by_locator)).click()

    def get_title(self,title):
        WebDriverWait(self.driver,15).until(EC.title_is(title))
        return self.driver.title


    def fluentWait(self,by_locator):
        wait = WebDriverWait(driver, 10, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        btn_search = wait.until(EC.element_to_be_clickable(by_locator)
        btn_search.click()
