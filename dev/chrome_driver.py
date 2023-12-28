import logging
import sys
from utils.log_config import setup_logger, handle_errors
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime
import json
from twilio.rest import Client

class Chrome_Driver:
    _chrome_driver_instance = None

    def __init__(self):
        self.custom_webdriver = self.setup_web_driver()
        setup_logger()


    @staticmethod
    def _get_chrome_options():
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        return opts

    @staticmethod
    def _get_chromedriver_executable_path():
        return '/opt/homebrew/bin/chromedriver'

    @classmethod
    def get_web_driver_instance(cls):
        if cls._chrome_driver_instance is None:
            cls._chrome_driver_instance = Chrome_Driver()
        return cls._chrome_driver_instance

    def setup_web_driver(self):
        logging.info('Initializing ChromeDriver with remote debugging')
        opts = self._get_chrome_options()
        chromedriver_exec_path = self._get_chromedriver_executable_path()

        web_driver = webdriver.Chrome(
            service=Service(executable_path=chromedriver_exec_path),
            options=opts
        )

        return web_driver



