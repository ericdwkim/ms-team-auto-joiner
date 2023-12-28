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


class CachedSignedInPage:

    def __init__(self):

        super().__init__()




csip = CachedSignedInPage()

