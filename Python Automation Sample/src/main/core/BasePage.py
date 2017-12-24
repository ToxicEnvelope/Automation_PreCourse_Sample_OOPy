#!/usr/bin/env python


import os
try:
	import sys
	import pip
	import time
	import unittest
	import selenium.common.exceptions.WebDriverException as wde
	from selenium import webdriver
	from selenium.webdriver.common.by import By
	from selenium.webdrier.common.keys import Keys
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
except ImportError as e:
	pip = lambda : os.system('pip install ' + str(e)[15:])
	pip()



# we can add on the tests section ClassName(unittest.TestCase) for testing implementations
class BasePage:

	def __init__(self, driver):
		this._driver = driver

	def click(self, element):
		try:
			self._driver.execute_script("argumets[0].setAttribute('sytle', 'borde: 2px solid green');")
			element.click()
		except wde as e:
			print str(e)
			self._driver.execute_script("argumets[0].setAttribute('sytle', 'borde: 2px solid green');")
			self._driver.execute_script("argumets[0].click();")


	def fill_text(self, element, word):
		try:
			self._driver.execute_script("argumets[0].setAttribute('sytle', 'borde: 2px solid blue');")
			element.send_keys(word)	
		except wde as e:
			self._driver.execute_script("argumets[0].setAttribute('sytle', 'borde: 2px solid blue');")
			self._driver.execute_script("argumets[0].vaule = " + word)

	def wait(self, sec):
		try:
			time.sleep(sec)
		except Exception as e:
			print str(e)

	def wait_until_visible_by_CSS(self, css):
		try:
			return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.selector(css))))
		except wde as e:
			print str(e)

	def wait_until_visible_by_ID(self, id):
		try:
			return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.id(id)))))	
		except wde as e:
			print str(e)
	def wait_until_presents_by_CSS(self, css):
		try:
			return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.selector(css))))
		except wde as e:
			print str(e)
	def wait_until_presents_by_ID(self, id):
		try:
			return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.id(id))))
		except wde as e:
			print str(e)
