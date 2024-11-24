import pytest

from Pages.login_page import LoginPage
from Tests.test_base import BaseTest
from Utilities.read_config import AppConfiguration
from playwright.sync_api import expect




class TestLogin(BaseTest):

    configuration = AppConfiguration.get_common_info()

    def get_user_credentials(self):
        return {
            "username": self.configuration["UserName"],
            "password": self.configuration["Password"]
        }
    
    def test_login_with_valid_credentials(self):

        self.login_page = LoginPage(self.page)
        credentials = self.get_user_credentials()

        invoice_page = self.login_page.login_to_application(credentials["username"],credentials["password"])
     
        expect(invoice_page.get_header_locator()).to_have_text("Invoice List")
    
    @pytest.mark.parametrize(
            "username, password",
            [
                ("Demouser", "abc123"),
                ("demouser_", "xyz"),
                ("demouser", "nananana"),
                ("demouser", "abc123")
            ]
    )
    def test_login_with_invalid_credentials(self, username, password):
        
        expected_error_msg = "Wrong username or password."

        self.login_page = LoginPage(self.page)

        self.login_page.login_to_application(username, password)

        expect(self.login_page.get_error_locator()).to_be_visible()
        expect(self.login_page.get_error_locator()).to_have_text(expected_error_msg)
        
