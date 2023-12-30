import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Chrome_Driver:
    _chrome_driver_instance = None

    def __init__(self):
        self.custom_webdriver = self.setup_web_driver()

    @classmethod
    def get_web_driver_instance(cls):
        if cls._chrome_driver_instance is None:
            cls._chrome_driver_instance = cls()
        return cls._chrome_driver_instance

    @staticmethod
    def _get_chrome_options():
        opts = webdriver.ChromeOptions()
        # opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # deving purposes until 2fa solution
        opts.add_argument('--start-maximized')
        return opts

    @staticmethod
    def _get_chromedriver_executable_path():
        return '/opt/homebrew/bin/chromedriver'


    def setup_web_driver(self):
        logging.info('Initializing ChromeDriver...')
        opts = self._get_chrome_options()
        chromedriver_exec_path = self._get_chromedriver_executable_path()

        web_driver = webdriver.Chrome(
            service=Service(executable_path=chromedriver_exec_path),
            options=opts
        )

        return web_driver



