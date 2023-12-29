import logging
import json
from src.app.chrome_driver import Chrome_Driver
from src.pages.base_page import BasePage


class Main:

    def __init__(self):
        self.conf = self.load_envs()

    @staticmethod
    def load_envs():
        with open('/Users/ekim/workspace/personal/MS-Teams-Auto-Joiner/config.json') as f:
            config = json.load(f)
            return config




if __name__ == "__main__":
    driver = Chrome_Driver().get_web_driver_instance().custom_webdriver
    conf = Main().conf
    page = BasePage(driver, conf)
    logging.info(page)
