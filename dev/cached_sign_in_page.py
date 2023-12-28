import logging
from sign_in_page import SignInPage
from time import sleep
from utils.log_config import handle_errors
from selenium.webdriver.common.by import By


class CachedSignedInPage(SignInPage):

    def __init__(self):

        super().__init__()

    @handle_errors
    def click_on_saved_account(self):
        account_selected = self.wait_and_find_element_and_click('//*[@id="tilesHolder"]/div[1]/div/div[1]/div/div[2]/div', By.XPATH)
        logging.info(f'Click on saved account attempt: {account_selected}')
        return account_selected  # return the bool whether true or false


account_selected = CachedSignedInPage().click_on_saved_account()
