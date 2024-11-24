from playwright.sync_api import Page, Locator
from dataclasses import dataclass

from Pages.base_page import BasePage
from Pages.invoice_page import InvoicePage

@dataclass
class Selectors:
    USERNAME = "input[name=\"username\"]"
    PASSWORD = "input[name=\"password\"]"
    LOGIN_BUTTON = "Login"
    ERROR_MSG = "[role=\"alert\"]"


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.selectors = Selectors()

    def set_username(self, value: str):
        self.current_page.fill(self.selectors.USERNAME, value)

    def set_password(self, value: str):
        self.current_page.fill(self.selectors.PASSWORD, value)

    def click_login(self):
        self.current_page.get_by_role("button", name = self.selectors.LOGIN_BUTTON).click()

    def login_to_application(self, username: str, password: str) -> InvoicePage:
        self.set_username(username)
        self.set_password(password)
        self.click_login()
        return InvoicePage(self.current_page)

    def get_error_locator(self) -> Locator:
        return self.current_page.locator(self.selectors.ERROR_MSG)

 
       


