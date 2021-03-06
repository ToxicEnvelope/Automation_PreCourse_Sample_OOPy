#!/usr/bin/env python


import os
import sys
try:
    paths = [os.getcwd()]
    for p in paths:
        os.chdir(p)
        current_dir = os.getcwd()
        sys.path.append(current_dir)
    import unittest
    from selenium import webdriver
    from src.main.core.utils import Logger, setup
    from src.main.core.pageobjects import FBPage
except ImportError as e:
    pip = lambda : os.system('pip install' + str(e)[15:])
    pip()


    
class BaseTest(unittest.TestCase):

    # loading all dependencies to PYTHONPATH
    setup.load()
    #chromedriver_path = "c:\\Users\\Home\\Desktop\\Python-Automation\\PythonAutomationSample\\src\\main\\execs\\chromedriver.exe"
    chromedriver_path = os.getcwd() + "/Python-Automation/PythonAutomationSample/src/main/exec/chromedriver"
    base_url_1 = "https://www.python.org"
    base_url = "https://www.facebook.com"
    logger = Logger()
    
    def setUp(self):
        try:
            self.logger.info("----- set up started -----")
            self.driver = webdriver.Chrome(self.chromedriver_path)
            self.logger.info("----- set up ended -----")
        except Exception as e:
            self.logger.critical("Unknown Exception in setUp!", e)


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
        try:
            self.logger.info("----- test started -----")
            driver = self.driver
            driver.get(self.base_url)
            fb_page = FBPage(driver)
            fb_page.attempt_to_authenticate("sysmurff@gmail.com", "Aa123456")
            self.logger.info("----- test ended -----")
        except Exception as e:
            self.logger.critical("Unknown Exception in Test RunTime!", e)

    def tearDown(self):
        try:
            self.logger.info("----- tear down started -----")
            self.driver.close()
            self.logger.info("----- tear down ended -----")
        except Exception as e:
            self.logger.critical("Unknown Exception in tearDown!", e)


if __name__ == "__main__":
    unittest.main()
