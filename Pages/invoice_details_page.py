from playwright.sync_api import Page, Locator
from dataclasses import dataclass

from Pages.base_page import BasePage
from Utilities.table_handler import TableHandler

@dataclass
class Selectors:
    HOTEL_NAME = "h4.mt-5"
    INVOICE_NUMBER = "h6.mt-2"
    INVOICE_DATE =  "li:has(span.font-weight-bold:text-is('Invoice Date:'))"
    DUE_DATE = "li:has(span.font-weight-bold:text-is('Due Date:'))"
    BOOKING_CODE = "//tr[td[contains(text(),'Booking Code')]]/td[2]"
    ROOM = "//tr[td[contains(text(),'Room')]]/td[2]"
    TOTAL_STAY_COUNT = "//tr[td[contains(text(),'Total Stay Count')]]/td[2]"
    TOTAL_STAY_AMOUNT = "//tr[td[contains(text(),'Total Stay Amount')]]/td[2]"
    CHECK_IN = "//tr[td[contains(text(),'Check-In')]]/td[2]"
    CHECK_OUT = "//tr[td[contains(text(),'Check-Out')]]/td[2]"
    CUSTOMER_DETAILS = "//h5[text()='Customer Details']/following-sibling::div"
    DEPOSIT_NOWT = "table.table:nth-of-type(2) tbody tr td:first-child"
    TAX_AND_VAT = "table.table:nth-of-type(2) tbody tr td:nth-of-type(2)"
    TOTAL_AMOUNT = "table.table:nth-of-type(2) tbody tr td:nth-of-type(3)"


class InvoiceDetailsPage(BasePage):
    def __init__(self, page: Page):
        """
        Initialize the InvoiceDetailsPage with the given page.
        
        Args:
            page (Page): The Playwright page instance used to interact with the page.
        """
        super().__init__(page)
        self.selectors = Selectors()

    def get_hotel_locator(self) -> Locator:
        """
        Get the locator for the hotel name on the invoice details page.
        
        Returns:
            Locator: The locator object for the hotel name element.
        """
        return self.current_page.locator(self.selectors.HOTEL_NAME)

    def get_invoice_date_locator(self) -> Locator:
        """
        Get the locator for the invoice date on the invoice details page.
        
        Returns:
            Locator: The locator object for the invoice date element.
        """
        return self.current_page.locator(self.selectors.INVOICE_DATE)
    
    def get_due_date_locator(self) -> Locator:
        """
        Get the locator for the due date on the invoice details page.
        
        Returns:
            Locator: The locator object for the due date element.
        """
        return self.current_page.locator(self.selectors.DUE_DATE)

    def get_invoice_number_locator(self) -> Locator:
        """
        Get the locator for the invoice number on the invoice details page.
        
        Returns:
            Locator: The locator object for the invoice number element.
        """
        return self.current_page.locator(self.selectors.INVOICE_NUMBER)
    
    def get_booking_code_locator(self) -> Locator:
        """
        Get the locator for the booking code on the invoice details page.
        
        Returns:
            Locator: The locator object for the booking code element.
        """
        return self.current_page.locator(self.selectors.BOOKING_CODE)
    
    def get_room_locator(self) -> Locator:
        """
        Get the locator for the room information on the invoice details page.
        
        Returns:
            Locator: The locator object for the room element.
        """
        return self.current_page.locator(self.selectors.ROOM)
    
    def get_check_in_locator(self) -> Locator:
        """
        Get the locator for the check-in date on the invoice details page.
        
        Returns:
            Locator: The locator object for the check-in date element.
        """
        return self.current_page.locator(self.selectors.CHECK_IN)
    
    def get_check_out_locator(self) -> Locator:
        """
        Get the locator for the check-out date on the invoice details page.
        
        Returns:
            Locator: The locator object for the check-out date element.
        """
        return self.current_page.locator(self.selectors.CHECK_OUT)
    
    def get_total_stay_count_locator(self) -> Locator:
        """
        Get the locator for the total stay count on the invoice details page.
        
        Returns:
            Locator: The locator object for the total stay count element.
        """
        return self.current_page.locator(self.selectors.TOTAL_STAY_COUNT)
    
    def get_total_stay_amount_locator(self) -> Locator:
        """
        Get the locator for the total stay amount on the invoice details page.
        
        Returns:
            Locator: The locator object for the total stay amount element.
        """
        return self.current_page.locator(self.selectors.TOTAL_STAY_AMOUNT)    
    
    def get_customer_details_locator(self) -> Locator:
        """
        Get the locator for the customer details section on the invoice details page.
        
        Returns:
            Locator: The locator object for the customer details element.
        """
        return self.current_page.locator(self.selectors.CUSTOMER_DETAILS)
    
    def get_deposit_nowt_locator(self) -> Locator:
        """
        Get the locator for the deposit now amount in the second table on the invoice details page.
        
        Returns:
            Locator: The locator object for the deposit now element.
        """
        return self.current_page.locator(self.selectors.DEPOSIT_NOWT)
    
    def get_tax_vat_locator(self) -> Locator:
        """
        Get the locator for the tax and VAT amount in the second table on the invoice details page.
        
        Returns:
            Locator: The locator object for the tax and VAT element.
        """
        return self.current_page.locator(self.selectors.TAX_AND_VAT)
    
    def get_total_amount_locator(self) -> Locator:
        """
        Get the locator for the total amount in the second table on the invoice details page.
        
        Returns:
            Locator: The locator object for the total amount element.
        """
        return self.current_page.locator(self.selectors.TOTAL_AMOUNT)
