#!/usr/bin/env python


import os
import sys
import unittest
from selenium import webdriver
from src.main.core.utils import Logger
from src.main.core.pageobjects import FBPage


    
class BaseTest(unittest.TestCase):

    chromedriver_path = "c:\\Users\\Home\\Desktop\\Python-Automation\\PythonAutomationSample\\src\\main\\execs\\chromedriver.exe"
    base_url_1 = "https://www.python.org"
    base_url = "https://www.facebook.com"
    logger = Logger()
    def setUp(self):
        logger.info("----- set up started -----")
        self.driver = webdriver.Chrome(self.chromedriver_path)
        logger.info("----- set up ended -----")


    #### TEST REFERENCE ####
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
        logger.info("----- test started -----")
        driver = self.driver
        driver.get(self.base_url)
        fb_page = FBPage(driver)
        fb_page.attempt_to_authenticate("sysmurff@gmail.com", "Aa123456")
        logger.info("----- test ended -----")

    def tearDown(self):
        logger.info("----- tear down started -----")
        self.driver.close()
        logger.info("----- tear down ended -----")



if __name__ == "__main__":
    unittest.main()