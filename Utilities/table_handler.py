from playwright.sync_api import Locator, Page

class TableHandler:
    def __init__(self, page: Page, table_selector: str):
        """
        Initialize the TableHandler with the given page and table selector.
        
        Args:
            page (Page): The Playwright page instance used to interact with the table.
            table_selector (str): The CSS selector used to locate the table on the page.
        """
        self.page = page
        self.table_selector = table_selector

    def get_row_locator(self, row_number: int) -> Locator:
        """
        Get the locator for a specific row in the table based on its index (row_number).
        
        Args:
            row_number (int): The row number (index) in the table to locate.
        
        Returns:
            Locator: The locator object for the specified row.
        """
        self.row_selector = f"{self.table_selector} .row:nth-of-type({row_number})"
        return self.page.locator(self.row_selector)
    
    def get_locator_by_label(self, label: str) -> Locator:
        """
        Get the locator for a table cell based on a label.
        
        Args:
            label (str): The label text used to identify the corresponding cell in the table.
        
        Returns:
            Locator: The locator object for the cell located by the label.
        """
        
        self.label_locator = self.page.locator(f"{self.table_selector} td.font-weight-bold:text('{label}')")
       
        return self.label_locator.locator(".. >> following-sibling:td")
