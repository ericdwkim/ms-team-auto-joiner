import logging
from src.pages.base_page import BasePage
import json
from src.utils.log_config import handle_errors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(BasePage):
    def __init__(self, driver, conf):
        super().__init__(driver, conf)

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
