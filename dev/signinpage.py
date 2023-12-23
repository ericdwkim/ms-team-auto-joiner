import logging
from drivers import Driver
import json
import sys
from utils.log_config import handle_errors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class SignInPage:
    def __init__(self):
        self.driver = Driver().get_webdriver()

    def load_envs(self):
        try:
            with open('/Users/ekim/workspace/personal/MS-Teams-Auto-Joiner/config.json', 'r') as f:
                config = json.load(f)
                if not config:
                    logging.error(f'Could not parse config.json properly')
                return config

        except:
            logging.exception('Could not locate config.json ... Exiting...')
            sys.exit(1)



    def find_element_and_click(self, locator ,locator_type=By.ID):
        """
        Finds element and clicks it using `WebElement.click()`
        :param locator:
        :param locator_type:
        :return: Tuple(bool, WebElement)
        """
        try:
            element = self.driver.find_element(locator_type, locator)
            element.click()
            return True, element
        except NoSuchElementException:
            logging.error(f'Element {locator} was not found.')
            return False, None
        except Exception as e:
            logging.exception(f'Error occurred when trying to find and click element: {str(e)}')
            return False, None

    def wait_and_find_element_and_click_and_send_keys(self, locator, keys_to_send):
        """
        Find element by locator string, click on element, and send keys
        :param locator:
        :param keys_to_send:
        :return: bool
        """
        try:
            elem_is_present = self.wait_for_element(locator, locator_type=By.ID)
            if not elem_is_present:
                logging.error(f'Could not wait for element on DOM')
                return
            was_clicked, element_selector_clicked = self.find_element_and_click(locator)
            if was_clicked:
                element_selector_clicked.send_keys(keys_to_send)
                return True
            else:
                logging.error(f'Failed to send keys to element: {locator}')
                return False
        except Exception as e:
            logging.exception(f'An error occurred trying to find_element_and_click_and_send_keys: {str(e)}')
            return False


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
            logging.exception(f'Tried waiting for element on DOM but timed out')
            return False # elem not found within allotted `timeout`


sip = SignInPage()

conf = sip.load_envs()

sip.wait_and_find_element_and_click_and_send_keys('i0116', conf['username'])
