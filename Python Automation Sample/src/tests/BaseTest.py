import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BaseTest(unittest.TestCase):

    chromedriver_path = "'c:\\Users\\Home\\Desktop\\Python-Automation\\src\\main\\execs\\chromedriver.exe'"
    # base_url = "https://www.python.org"
    base_url = "https://www.facebook.com"

    def setUp(self):
        self.driver = webdriver.Chrome(self.chromedriver_path)

    # def test_search_in_python_org(self):
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     self.assertIn("Python", driver.title)
    #     elem = driver.find_element_by_name("q")
    #     elem.send_keys("pycon")
    #     elem.send_keys(Keys.RETURN)
    #     assert "No results found." not in driver.page_source

    # Test a simple session login / authentication with FB site
    def TEST_FB_LOGIN(self):
        self.driver.get(self.base_url)
        fb_page = FBPage(self.driver)
        fb.attempt_to_authenticate("sysmurff@gmail.com", "Aa123456")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()