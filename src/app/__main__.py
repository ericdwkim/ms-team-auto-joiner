import logging
import json
from time import sleep
from src.utils.log_config import setup_logger, handle_errors
from selenium.webdriver.common.by import By
from src.app.chrome_driver import Chrome_Driver
from src.pages.base_page import BasePage
from src.pages.sign_in_page import SignInPage
from src.pages.cached_sign_in_page import CachedSignedInPage
from selenium.common.exceptions import StaleElementReferenceException


class App:

    def __init__(self):
        setup_logger()
        self.driver = Chrome_Driver.get_web_driver_instance().custom_webdriver
        self.conf = self.load_envs()
        self.base_page = BasePage(self.driver, self.conf)
        self.regular_sign_in = SignInPage(self.driver, self.conf)
        self.cached_sign_in = CachedSignedInPage(self.driver, self.conf)

    @staticmethod
    def load_envs():
        with open('/Users/ekim/workspace/personal/MS-Teams-Auto-Joiner/config.json') as f:
            config = json.load(f)
            return config
    @handle_errors
    def sign_in(self):
        # Launch webapp
        self.base_page.visit()
        # `Sign In` button
        if self.base_page.wait_for_element('idSIButton9', By.ID):
            reg_logged_in = self.regular_sign_in.login()
            logging.info(f'Regular logged in status: {reg_logged_in}')
            return reg_logged_in
        cached_logged_in = self.cached_sign_in.login()
        logging.info(f'Cached logged in status: {cached_logged_in}')
        return cached_logged_in

    @handle_errors
    def sign_in_submit_post_2fa(self):
        sleep(15)  # wait for manual 2fa

        # Loop until "Stay signed in?" to be on page indicating we passed 2fa manuallyZ
        if 'Stay signed in?' in self.driver.page_source:
            try:
                # `Yes` sign in submit button
                if self.base_page.wait_and_find_element_and_click('idSIButton9', By.ID):
                    logging.info('Could not wait, find, and click Yes button')
                    return True
            except StaleElementReferenceException:
                try:
                    self.base_page.wait_and_find_element_and_click('//*[@class="win-button button_primary button ext-button primary ext-primary"]', By.CLASS_NAME)
                    logging.info('Could not wait, find, and click Yes button with classname')
                    return True

                finally:
                    self.base_page.wait_and_find_element_and_click('//*[@id="idSIButton9"]', By.XPATH)
                    logging.info('Successfully wait, find, and click Yes')
                    return True


if __name__ == "__main__":
    app = App()
    app.sign_in()
    app.sign_in_submit_post_2fa()
