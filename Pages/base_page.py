from playwright.sync_api import Page, Locator


class BasePage:
    
    def __init__(self, page : Page):
        self.current_page = page

