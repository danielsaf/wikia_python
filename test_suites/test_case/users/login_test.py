

__author__ = 'dsafinski'
# -*- coding: utf-8 -*-
import unittest
import test_suites
from test_suites.pages.login_page import Locators
from holmium.core import TestCase


class LoginTest(TestCase):
    def setUp(self):
        self.login_page = test_suites.pages.login_page.LoginPage(self.driver, self.config['base_url'])

    def test_login_with_good_credential(self):
        self.login_page.login('TestDaniel', 'Test123')
        assert 'TestDaniel - My page' in self.driver.page_source

    def test_login_with_wrong_username(self):
        self.login_page.login('TestDanielFail', 'Test123')
        assert "Hm, we don't recognize this name. Don't forget usernames are case sensitive." in self.driver.page_source

    def test_login_with_wrong_password(self):
        self.login_page.login('TestDaniel', 'Test123Fail')
        assert 'Oops, wrong password. Make sure caps lock is off and try again.' in self.driver.page_source

    # def test_login_with_no_credential(self):
    #     self.login_page.login('', '')
    #     assert 'Oops, please fill in the username field.' in self.driver.page_source


if __name__ == "__main__":
    unittest.main()
