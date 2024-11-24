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
        """
        Initialize the LoginPage with the given page instance and set up the selectors.
        
        Args:
            page (Page): The Playwright page instance used to interact with the login page.
        """
        super().__init__(page)
        self.selectors = Selectors()

    def set_username(self, value: str):
        """
        Set the username value in the username input field.
        
        Args:
            value (str): The username to be entered in the username input field.
        """
        self.current_page.fill(self.selectors.USERNAME, value)

    def set_password(self, value: str):
        """
        Set the password value in the password input field.
        
        Args:
            value (str): The password to be entered in the password input field.
        """
        self.current_page.fill(self.selectors.PASSWORD, value)

    def click_login(self):
        """
        Click the login button to attempt to log into the application.
        """
        self.current_page.get_by_role("button", name=self.selectors.LOGIN_BUTTON).click()

    def login_to_application(self, username: str, password: str) -> InvoicePage:
        """
        Perform the login action by entering the username and password, and then clicking the login button.
        
        Args:
            username (str): The username for login.
            password (str): The password for login.
        
        Returns:
            InvoicePage: After a successful login, this method returns an instance of the InvoicePage.
        """
        self.set_username(username)
        self.set_password(password)
        self.click_login()
        return InvoicePage(self.current_page)

    def get_error_locator(self) -> Locator:
        """
        Get the locator for the error message, if any, displayed on the login page.
        
        Returns:
            Locator: The locator object for the error message element.
        """
        return self.current_page.locator(self.selectors.ERROR_MSG)
