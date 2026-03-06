class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def fill_input(self, selector, text):
        self.page.locator(selector).fill(text)

    def click_element(self, selector):
        self.page.locator(selector).click()

    def get_text(self, selector):
        return self.page.locator(selector).inner_text()