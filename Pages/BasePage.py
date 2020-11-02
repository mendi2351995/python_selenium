from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import time
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


    def fluentWait_click(self,by_locator):
        wait = WebDriverWait(self.driver, 10, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        btn_search = wait.until(EC.element_to_be_clickable(by_locator))
        btn_search.click()

#   Receives only element and not by
    def wait_for_element_to_vanish(self,by_locator: WebElement)-> bool:
        is_displaye = by_locator.is_displayed()
        start_time = self.get_current_time_in_millis()
        time_interval_in_seconds = 5
        while is_displaye and not self.is_time_out(start_time,time_interval_in_seconds):
            is_displaye = by_locator.is_displayed()
        return not is_displaye
    def is_time_out(self,start_time_millis: int,waiting_interval_seconds: int)-> bool:
        end_time = start_time_millis + waiting_interval_seconds * 1000
        return self.get_current_time_in_millis() > end_time
    def get_current_time_in_millis(self)-> int:
        return int(time.time() * 1000)

    def multiselect_set_selections(self,element, labels):
        # element = self.driver.find_element_by_xpath(element)
        for option in element.find_elements_by_tag_name('option'):
            print(option.text)
            if option.text in labels:
                print(option.text, " clickkkkk")
                option.click()

    def select_value_on_DropDwon(self,drop_list,value):
        for ele in drop_list:
            for k in range(len(drop_list)):
                if ele.text == value[k]:
                    ele.click()
                    break
                  
    def popUp_Alert_text(self):
        alert = self.driver.switch_to.alert
        t = alert.text
        self.switch_to_default_content()
        return t
    def popUp_Alert_Accept(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        self.switch_to_default_content()
    def popUp_Alert_dismiss(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()
        self.switch_to_default_content()
    def popUp_Alert(self,text):
        alert = self.driver.switch_to.alert
        alert.send_keys()
        self.switch_to_default_content(text)