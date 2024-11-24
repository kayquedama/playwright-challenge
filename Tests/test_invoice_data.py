import pytest
from Tests.test_base import BaseTest
from Pages.login_page import LoginPage
from Pages.invoice_page import InvoicePage
from Utilities.read_config import AppConfiguration
from playwright.sync_api import expect


class TestInvoiceData(BaseTest):

    configuration = AppConfiguration.get_common_info()

    def get_user_credentials(self):
        return {
            "username": self.configuration["UserName"],
            "password": self.configuration["Password"]
        }
    
    @pytest.fixture(autouse=True)
    def setup_login(self, setup):
        self.page = setup
        self.login_page = LoginPage(self.page)
        credentials = self.get_user_credentials()

        invoice_page = self.login_page.login_to_application(credentials["username"],credentials["password"])
     
        expect(invoice_page.get_header_locator()).to_have_text("Invoice List")

    def test_invoice_data_number_110(self):

        self.invoice_page = InvoicePage(self.page)

        self.invoice_details = self.invoice_page.go_to_first_invoice_details()

        expect(self.invoice_details.get_hotel_locator()).to_have_text("Rendezvous Hotel")
        expect(self.invoice_details.get_invoice_date_locator()).to_contain_text("14/01/2018")
        expect(self.invoice_details.get_due_date_locator()).to_contain_text("15/01/2018")
        expect(self.invoice_details.get_invoice_number_locator()).to_contain_text("110")
        expect(self.invoice_details.get_booking_code_locator()).to_have_text("0875")
        expect(self.invoice_details.get_customer_details_locator()).to_contain_text("JOHNY SMITH")
        expect(self.invoice_details.get_customer_details_locator()).to_contain_text("R2, AVENUE DU MAROC")
        expect(self.invoice_details.get_customer_details_locator()).to_contain_text("123456")
        expect(self.invoice_details.get_room_locator()).to_have_text("Superior Double")
        expect(self.invoice_details.get_check_in_locator()).to_have_text("14/01/2018")
        expect(self.invoice_details.get_check_out_locator()).to_have_text("15/01/2018")
        expect(self.invoice_details.get_total_stay_count_locator()).to_have_text("1")
        expect(self.invoice_details.get_total_stay_amount_locator()).to_have_text("$150")
        expect(self.invoice_details.get_deposit_nowt_locator()).to_have_text("USD $20.90")
        expect(self.invoice_details.get_tax_vat_locator()).to_have_text("USD $19")
        expect(self.invoice_details.get_total_amount_locator()).to_have_text("USD $209")