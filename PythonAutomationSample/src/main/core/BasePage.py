#!/usr/bin/env python


import os
try:
	import sys
	import pip
	import time
	import unittest

	paths = ['/']
	for p in paths:
		os.chdir(p)
		current_dir = os.getcwd()
		sys.path.append(current_dir)

	from selenium import webdriver
	from selenium.common.exceptions import WebDriverException
	########
	# online reference -> https://pythonselenium.blogspot.co.il/2014/12/logging-exception-in-selenium.html
	# Logger for selenium in python
	from src.main.core.utils import Logger
	from selenium.webdriver.common.by import By
	from selenium.webdrier.common.keys import Keys
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
except ImportError as e:
	pip = lambda : os.system('pip install ' + str(e)[15:])
	pip()




# feed object to BasePage (PageFactory) -> find_by <- 
class BasePage(object):

	# CONSTRUCTOR
	def __init__(self, driver):
		self._driver = driver
		self._logger = Logger.__init__(self)

	# CLICK on WebElement
	def click(self, element):
		try:
			self._driver.execute_script("argumets[0].setAttribute('sytle', 'borde: 2px solid green');")
			element.click()
			self._logger.info("----- element clicked by Selenium -----")
			self.wait(1)
		except WebDriverException as e:
			print str(e)
			self._driver.execute_script("argumets[0].setAttribute('sytle', 'borde: 2px solid green');")
			self._driver.execute_script("argumets[0].click();")
			self._logger.info("----- element clicked by JavaScript -----")
			self.wait(1)

	# FILL_TEXT to WebElement given String 
	def fill_text(self, element, word):
		try:
			self._driver.execute_script("argumets[0].setAttribute('sytle', 'borde: 2px solid blue');")
			element.send_keys(word)	
			self._logger.info("----- text filled by Selenium -----")
			self.wait(1)
		except WebDriverException as e:
			self._driver.execute_script("argumets[0].setAttribute('sytle', 'borde: 2px solid blue');")
			self._driver.execute_script("argumets[0].vaule = " + word)
			self._logger.info("----- text filled by Javascript -----")
			self.wait(1)

	# TAKE SCREEN SHOTS
	def snap(self):
		try:
			shadow = self.get_timestamp() + ".png"
			self._driver.get_screenshot_as_file(shadow)
			self._logger.info("----- took picture : "+ str(shadow) +" -----")
		except Exception as e:
			self._logger.critical("'Invalid Input : " + str(e))

	# WAIT 'x' seconds
	def wait(self, sec):
		try:
			time.sleep(sec)
		except Exception as e:
			self._logger.critical("Invalid Input : " + str(e))

	# WAIT for WebElement until is visible in DOM given cssSelector
	def wait_until_visible_by_CSS(self, css):
		try:
			self._logger.info("----- wait visible by : "+ str(css) +" -----")
			return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.selector(css))))
		except WebDriverException as e:
			self._logger.critical("'Invalid Input : " + str(e))

	# WAIT for WebElement until is present in DOM given id
	def wait_until_visible_by_ID(self, id):
		try:
			self._logger.info("----- wait visible by : "+ str(id) +" -----")
			return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.id(id))))
		except WebDriverException as e:
			self._logger.critical("'Invalid Input : " + str(e))

	# WAIT for WebElement until is visible in DOM given cssSelector
	def wait_until_presents_by_CSS(self, css):
		try:
			self._logger.info("----- wait presence by : "+ str(css) +" -----")
			return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.selector(css))))
		except WebDriverException as e:
			self._logger.critical("'Invalid Input : "+ str(e))

	# WAIT for WebElement until is present in DOM given id
	def wait_until_presents_by_ID(self, id):
		try:
			self._logger.info("----- wait present by : "+ str(id) +" -----")
			return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.id(id))))
		except WebDriverException as e:
			self._logger.critical("'Invalid Input : "+ str(e))

	# PRIVATE USE
	def get_timestamp(self):
		try:
			mark = time.asctime()
			self._logger.info("----- timestamp marked : "+ mark +" -----")
			return mark
		except Exception as e:
			self._logger.critical("'Invalid Input : " + str(e))
