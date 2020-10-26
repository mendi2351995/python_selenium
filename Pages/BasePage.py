from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver = driver


    def do_click(self,by_locator):
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(by_locator)).click()

    def get_title(self,title):
        WebDriverWait(self.driver,15).until(EC.title_is(title))
        return self.driver.title
