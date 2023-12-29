import logging
from time import sleep
from src.utils.log_config import handle_errors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, conf):
        self.driver = driver
        self.conf = conf

    @handle_errors
    def visit(self):
        logging.info(f'Visiting Teams Calendar Web...')
        self.driver.get('https://teams.microsoft.com/_\#/calendarv2')
        sleep(60)  # wait for unknown `.get` extreme lag/delay to load all DOMs on page

    @handle_errors
    def find_element_and_click(self, locator ,locator_type=By.ID):
        """
        Finds element and clicks it using `WebElement.click()`
        :param locator:
        :param locator_type:
        :return: Tuple(bool, WebElement)
        """
        element = self.driver.find_element(locator_type, locator)
        element.click()
        return (True, element)

    @handle_errors
    def wait_and_find_element_and_click_and_send_keys(self, locator, keys_to_send):
        """
        Find element by locator string, click on element, and send keys
        :param locator:
        :param keys_to_send:
        :return: bool
        """
        elem_is_present = self.wait_for_element(locator, locator_type=By.ID)
        if not elem_is_present:
            logging.error(f'Tried waiting for element using locator: "{locator}"')
            return False
        found_and_clicked, elem = self.find_element_and_click(locator)
        if found_and_clicked:
            elem.send_keys(keys_to_send)
            return True
        else:
            logging.error(f'Failed to send keys to element: {locator}')
            return False

    @handle_errors
    def wait_for_element(self, locator, locator_type, timeout=15):

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((locator_type, locator))
        )
        return True

    @handle_errors
    def wait_and_find_element_and_click(self, locator, locator_type):

        elem_is_present = self.wait_for_element(locator, locator_type)
        if not elem_is_present:
            logging.error(f'Tried waiting for element using locator: "{locator}"')
            return False
        found_and_clicked, elem = self.find_element_and_click(locator, locator_type)
        if found_and_clicked and elem:
            elem.click()
            return True
