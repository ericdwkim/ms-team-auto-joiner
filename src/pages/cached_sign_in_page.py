import logging
from src.pages.sign_in_page import SignInPage
from src.utils.log_config import handle_errors
from selenium.webdriver.common.by import By


class CachedSignedInPage(SignInPage):

    def __init__(self, driver, conf):
        super().__init__(driver, conf)

    @handle_errors
    def login_with_cached_session(self):
        account_selected = self.wait_and_find_element_and_click('//*[@id="tilesHolder"]/div[1]/div/div[1]/div/div[2]/div', By.XPATH)
        if not account_selected:
            logging.error(f'Could not click on saved account username\nClick on saved account attempt: {account_selected}')
            return account_selected
        pw_entered = self.enter_password()
        if not pw_entered:
            logging.error(f'Could not enter password during login attempt via cached session')
            return pw_entered
        elif account_selected and pw_entered:
            return True



# logged_in_via_cached_session = CachedSignedInPage().login_with_cached_session()
