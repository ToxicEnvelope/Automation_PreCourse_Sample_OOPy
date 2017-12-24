#!/usr/bin/env python


import os
import sys
import unittest
from selenium import webdriver
from .core.pageobjects.FBPage import *
#from selenium.webdriver.common.keys import Keys <---> simulate key events


class BaseTest(unittest.TestCase):

    chromedriver_path = "c:\\Users\\Home\\Desktop\\Python-Automation\\PythonAutomationSample\\src\\main\\execs\\chromedriver.exe"
    base_url_1 = "https://www.python.org"
    base_url = "https://www.facebook.com"

    def setUp(self):
        self.driver = webdriver.Chrome(self.chromedriver_path)

    # def test_search_in_python_org(self):
    #     driver = self.driver
    #     driver.get(self.base_url_1)
    #     self.assertIn("Python", driver.title)
    #     elem = driver.find_element_by_name("q")
    #     elem.send_keys("pycon")
    #     elem.send_keys(Keys.RETURN)
    #     assert "No results found." not in driver.page_source

    # Test a simple session login / authentication with FB site
    def test_fb_login(self):
        driver = self.driver
        driver.get(self.base_url)
        fb_page = FBPage(driver)
        fb_page.attempt_to_authenticate("sysmurff@gmail.com", "Aa123456")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()