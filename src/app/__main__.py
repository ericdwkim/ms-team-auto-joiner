import logging
import json
from src.utils.log_config import handle_errors
from selenium.webdriver.common.by import By
from src.app.chrome_driver import Chrome_Driver
from src.pages.base_page import BasePage
from src.pages.sign_in_page import SignInPage
from src.pages.cached_sign_in_page import CachedSignedInPage


class Main:

    def __init__(self):
        self.driver = Chrome_Driver().get_web_driver_instance().custom_webdriver
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
        # check to see if cached account element does not exist on DOM
        if not self.base_page.wait_for_element('//*[@id="tilesHolder"]/div[1]/div/div[1]/div/div[2]/div'):
            reg_logged_in = self.regular_sign_in.login()
            logging.info(f'Regular logged in status: {reg_logged_in}')
            return reg_logged_in
        cached_logged_in = self.cached_sign_in.login()
        logging.info(f'Cache logged in status: {cached_logged_in}')
        return cached_logged_in





if __name__ == "__main__":
    main_obj = Main()
    main_obj.sign_in()