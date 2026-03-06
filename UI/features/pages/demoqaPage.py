from pages.basePage import BasePage

class TextBoxPage(BasePage):
    URL = "https://demoqa.com/text-box"
    FULL_NAME_INPUT = "#userName"
    EMAIL_INPUT = "#userEmail"
    CURRENT_ADDRESS_INPUT = "#currentAddress"
    PERMANENT_ADDRESS_INPUT = "#permanentAddress"
    SUBMIT_BUTTON = "#submit"
    OUTPUT_BOX = "#output"

    def __init__(self, page):
        super().__init__(page)

    def go_to_page(self):
        self.navigate(self.URL)

    def fill_form(self, name, email, current_address, permanent_address):
        self.fill_input(self.FULL_NAME_INPUT, name)
        self.fill_input(self.EMAIL_INPUT, email)
        self.fill_input(self.CURRENT_ADDRESS_INPUT, current_address)
        self.fill_input(self.PERMANENT_ADDRESS_INPUT, permanent_address)

    def submit_form(self):
        self.page.locator(self.SUBMIT_BUTTON).scroll_into_view_if_needed()
        self.click_element(self.SUBMIT_BUTTON)

    def get_output_text(self):
        return self.get_text(self.OUTPUT_BOX)