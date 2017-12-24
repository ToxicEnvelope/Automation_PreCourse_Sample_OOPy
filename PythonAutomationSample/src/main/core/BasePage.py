#!/usr/bin/env python


import os
try:
	import sys
	import pip
	import time
	import unittest
	import selenium.common.exceptions.WebDriverException as wde
	from selenium import webdriver
	# online reference -> https://jeremykao.wordpress.com/2015/06/10/pagefactory-pattern-in-python/
	# PageFactory Pattern
	from pageobject_support import cacheable, callable_find_by as find_by
	########
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
		this._driver = driver

	# CLICK on WebElement
	def click(self, element):
		try:
			self._driver.execute_script("argumets[0].setAttribute('sytle', 'borde: 2px solid green');")
			element.click()
			wait(1)
		except wde as e:
			print str(e)
			self._driver.execute_script("argumets[0].setAttribute('sytle', 'borde: 2px solid green');")
			self._driver.execute_script("argumets[0].click();")
			wait(1)

	# FILL_TEXT to WebElement given String 
	def fill_text(self, element, word):
		try:
			self._driver.execute_script("argumets[0].setAttribute('sytle', 'borde: 2px solid blue');")
			element.send_keys(word)	
			wait(1)
		except wde as e:
			self._driver.execute_script("argumets[0].setAttribute('sytle', 'borde: 2px solid blue');")
			self._driver.execute_script("argumets[0].vaule = " + word)
			wait(1)

	# TAKE SCREEN SHOTS
	def snap():
		try:
			self._driver.get_screenshot_as_file(get_timestamp() + ".png")
		except Exception as e:
			print str(e)

	# WAIT 'x' seconds
	def wait(self, sec):
		try:
			time.sleep(sec)
		except Exception as e:
			print str(e)

	# WAIT for WebElement until is visible in DOM given cssSelector
	def wait_until_visible_by_CSS(self, css):
		try:
			return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.selector(css))))
		except wde as e:
			print str(e)

	# WAIT for WebElement until is present in DOM given id
	def wait_until_visible_by_ID(self, id):
		try:
			return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.id(id)))))	
		except wde as e:
			print str(e)

	# WAIT for WebElement until is visible in DOM given cssSelector
	def wait_until_presents_by_CSS(self, css):
		try:
			return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.selector(css))))
		except wde as e:
			print str(e)

	# WAIT for WebElement until is present in DOM given id
	def wait_until_presents_by_ID(self, id):
		try:
			return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.id(id))))
		except wde as e:
			print str(e)

	# PRIVATE USE
	def get_timestamp():
		try:
			return time.asctime()
		except Exception as e:
			print str(e)