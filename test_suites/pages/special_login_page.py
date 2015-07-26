__author__ = 'Daniel'
from holmium.core import Page, Element, Locators
from selenium.webdriver.support import wait

class SpecialLoginPage(Page):
    username_div = Element(Locators.CSS_SELECTOR,
                           '#mw-content-text > div > form > fieldset > div.input-group.error.required > div')
    password_div = Element(Locators.CSS_SELECTOR,
                           'div.input-group.password-input.error.required > div')

    def special_login_username_page(self):
        self.get_()
