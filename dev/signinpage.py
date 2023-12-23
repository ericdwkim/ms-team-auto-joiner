import logging
from drivers import Driver
from utils.log_config import handle_errors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class SignInPage:
    def __init__(self):
        self.driver = Driver()

    def wait_for_element(self, locator, locator_type, timeout=30):
        """
        Waits for elem via `locator` string using locator_type with a default timeout in secs
        :param locator:
        :param locator_type:
        :param timeout:
        :return: bool
        """

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((locator_type, locator))
            )
            return True # elem found
        except TimeoutException:
            return False # elem not found within allotted `timeout`


    def wait_and_find_elems_by_class(self, locator_type, class_name):
        """
        After a set delay, find and locate elements by class_name and return list of WebElements from DOM
        :param class_name:
        :return: list[WebElements]
        """

        try:
            are_elems_present = self.wait_for_element(class_name, locator_type)
            elems = self.driver.browser.find_elements(By.CLASS_NAME, class_name)
        except:
            logging.exception('exception in wait_and_find_elems_by_class')

        else:
            logging.info(f'Found list of elements: {elems} using class name: {class_name}')
            if not are_elems_present:
                logging.error(f'wait_and_find_elems_by_class error')
            return elems



sip = SignInPage()

sip.wait_and_find_elems_by_class('form-control ltr_override input ext-input text-box ext-text-box')