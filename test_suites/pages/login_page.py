__author__ = 'dsafinski'

from selenium.webdriver.common.action_chains import ActionChains
from holmium.core import Page, Element, Locators
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(Page):
    username = Element(Locators.NAME, 'username')
    password = Element(Locators.NAME, 'password')
    login_button = Element(Locators.CSS_SELECTOR,
                           '#UserLoginDropdown > form > fieldset > div.input-group.login-button > input')
    login_navigation = Element(Locators.ID, 'AccountNavigation')
    username_div = Element(Locators.CSS_SELECTOR,
                           '#mw-content-text > div > form > fieldset > div.input-group.error.required > div')
    password_div = Element(Locators.CSS_SELECTOR,
                           'div.input-group.password-input.error.required > div')

    def hover_over(self, element):
        self.action = ActionChains(self.driver)
        self.action.move_to_element(element).click().perform()

    def wait_for_window(self, ellement):
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(ellement)

    def login(self, username, password):
        self.hover_over(self.login_navigation)
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()
