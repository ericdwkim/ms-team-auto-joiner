import logging
import sys
from utils.log_config import setup_logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime
import json
from twilio.rest import Client

class Driver:
    def __init__(self):
        self.setup_driver()
        setup_logger()


    def setup_driver(self):
        logging.info('Initializing ChromeDriver with remote debugging')
        opts = self._get_chrome_options()
        chromedriver_exec_path = self._get_chromedriver_executable_path()

        self.browser = webdriver.Chrome(
            service=Service(executable_path=chromedriver_exec_path),
            options=opts
        )


    def _get_chrome_options(self):
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        return opts

    def _get_chromedriver_executable_path(self):
        return '/opt/homebrew/bin/chromedriver'


# driver = Driver()

# logging.info(driver)


class SignInPage:
    def __init__(self):
        self.driver = Driver()
    def wait_and_find_elems_by_class(self, class_name):
        sleep(30)
        try:
            elems = self.driver.browser.find_elements(By.CLASS_NAME, class_name)
        except:
            logging.exception('exception in wait_and_find_elems_by_class')

        else:
            logging.info(f'elems: {elems}')
            return elems






