import logging
from chrome_driver import Chrome_Driver
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
        # @dev: invoke instance method from custom base Driver class and access the pre-configured custom webdriver class attribute via Singleton Pattern
        self.driver = Chrome_Driver().get_web_driver_instance().custom_webdriver
        self.conf = self.load_envs()

    @staticmethod
    def load_envs():
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

    @handle_errors
    def enter_username(self):
        usrname_added = self.wait_and_find_element_and_click_and_send_keys('i0116', self.conf['username'])
        next_btn_clicked = self.find_element_and_click('idSIButton9', By.ID)
        if not usrname_added and not next_btn_clicked:
            logging.error('Could not enter username')
            return False
        elif usrname_added and not next_btn_clicked:
            logging.error('Added username, but could not click next button')
            return False
        return True

    @handle_errors
    def enter_password(self):
        pw_added = self.wait_and_find_element_and_click_and_send_keys('i0118', self.conf['password'])
        next_btn_clicked = self.find_element_and_click('idSIButton9', By.ID)
        if not pw_added and not next_btn_clicked:
            logging.error('Could not enter password')
            return False
        elif pw_added and not next_btn_clicked:
            logging.error('Added password, but could not click next button')
            return True
        return True

    @handle_errors
    def login(self):
        username_entered = self.enter_username()
        pw_entered = self.enter_password()
        if not username_entered and not pw_entered:
            logging.error('Username and Password could not be entered during login() attempt')
            return False
        elif username_entered and not pw_entered:
            logging.error('Username entered. Password could not be entered during login()')
            return False
        else:
            logging.info('Successfully logged in!')
            return True
