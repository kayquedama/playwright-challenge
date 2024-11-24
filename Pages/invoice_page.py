from playwright.sync_api import Page, Locator
from dataclasses import dataclass

from Pages.base_page import BasePage
from Pages.invoice_details_page import InvoiceDetailsPage
from Utilities.table_handler import TableHandler

@dataclass
class Selectors:
    HEADER_NAME = ".mt-5"
    INVOICE_TABLE = ".container"
    INVOICE_DETAILS_LINK = "a:has-text(\"Invoice Details\")"


class InvoicePage(BasePage):

    def __init__(self, page: Page):
        """
        Initialize the InvoicePage with the given page and set up selectors and table handler.
        
        Args:
            page (Page): The Playwright page instance used to interact with the page.
        """
        super().__init__(page)
        self.selectors = Selectors()
        self.invoice_list = TableHandler(page, self.selectors.INVOICE_TABLE)

    def get_header_locator(self) -> Locator:
        """
        Get the locator for the page header.
        
        Returns:
            Locator: The locator object for the page header element.
        """
        return self.current_page.locator(self.selectors.HEADER_NAME)

    def click_invoice_details(self, row_locator: Locator) -> InvoiceDetailsPage: 
        """
        Click the 'Invoice Details' link for a specific row and navigate to the InvoiceDetailsPage.
        
        Args:
            row_locator (Locator): The locator for the row that contains the 'Invoice Details' link.
        
        Returns:
            InvoiceDetailsPage: A new InvoiceDetailsPage instance representing the page that is opened.
        """
        row_locator.locator(self.selectors.INVOICE_DETAILS_LINK).click()
        self.new_page = self.current_page.context.wait_for_event("page") 
        return InvoiceDetailsPage(self.new_page)
        
    def go_to_first_invoice_details(self) -> InvoiceDetailsPage:
        """
        Navigate to the first invoice details page by selecting the first row in the invoice table.
        
        Returns:
            InvoiceDetailsPage: A new InvoiceDetailsPage instance representing the first invoice details page.
        """
        self.row = self.invoice_list.get_row_locator(2)  
        return self.click_invoice_details(self.row)
