import logging
from drivers import Driver
import json
from time import sleep
import sys
from utils.log_config import handle_errors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class SignInPage:
    def __init__(self):
        self.driver = Driver().get_webdriver()

    @handle_errors
    def load_envs(self):
        with open('/Users/ekim/workspace/personal/MS-Teams-Auto-Joiner/config.json', 'r') as f:
            config = json.load(f)
            return config

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


sip = SignInPage()

conf = sip.load_envs()

# test = sip.wait_for_element('i0116', By.ID)

sip.wait_and_find_element_and_click_and_send_keys('i0116', conf['username'])
next_btn_clicked = sip.wait_and_find_element_and_click('idSIButton9', By.ID)
sleep(30)
sip.wait_and_find_element_and_click_and_send_keys('i0118', conf['password'])
next_btn_clicked2 = sip.wait_and_find_element_and_click('idSIButton9', By.ID)

