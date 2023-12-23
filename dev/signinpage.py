import logging
from drivers import Driver
from utils.log_config import handle_errors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class SignInPage:
    def __init__(self):
        self.driver = Driver().get_webdriver()

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

    # def wait_for_and_find_element(self, locator, locator_type, timeout):
    #     try:
    #         wait = self.wait_for_element(locator, locator_type, timeout)
    #         if not wait:
    #             logging.error(f'Tried to wait to locate element via locator "{locator}", but timed out. Please re-run the script with the cursor and screen focus on the Chrome Browser.')
    #             return False, None
    #         element = self.driver.find_element(locator_type, locator)
    #         if not element:
    #             logging.error(f'Could not find element via locator "{locator}"')
    #             return True, None
    #         if wait and element:
    #             logging.info(f'Found and located element via locator "{locator}"')
    #             return True, element
    #
    #     except Exception as NoSuchElementException:
    #         logging.exception(f'An unexpected error occurred: {NoSuchElementException}')

    def wait_and_find_elems_by_id(self, locator, locator_type=By.ID):

        try:
            elem_is_present = self.wait_for_element(locator, locator_type)
            elem = self.driver.find_element(By.ID, locator)
        except:
            logging.exception('exception in wait_and_find_elems_by_id')

        else:
            logging.info(f'Found element: {elem} using ID: "{locator}"')
            if not elem_is_present:
                logging.error(f'wait_and_find_elems_by_id error')
            return elem



sip = SignInPage()

usrname_txtbox_elem = sip.wait_and_find_elems_by_id('i0116')
logging.info(usrname_txtbox_elem)


