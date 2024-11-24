from playwright.sync_api import Page, Locator
from dataclasses import dataclass

from Pages.base_page import BasePage

@dataclass
class Selectors:
    HEADER_NAME = ".mt-5"
    PASSWORD = "input[name=\"password\"]"
    LOGIN_BUTTON = "Login"
    ERROR_MSG = "Wrong username or password."


class InvoicePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.selectors = Selectors()

    def get_header_locator(self) -> Locator:
        return self.current_page.locator(self.selectors.HEADER_NAME)
