#!/usr/bin/env python 

import os
#Import the logging module
import logging

class Logger:


	def __init__(self):
		self.init()

	# Initializer
	def init(self):
		self._logger = logging.getLogger(__name__)
		self._logger.setLevel(logging.INFO)
		#Create a file handler
		#self._handler_warn = logging.FileHandler('c:\\Users\\Home\\Desktop\\Python-Automation\\PythonAutomationSample\\src\\tests\\results\\log\\warning_log.txt')
		self._handler_warn = logging.FileHandler( os.getcwd() + "/src/tests/results/log/warning_log.txt")
		self._handler_warn.setLevel(logging.WARNING)
		#self._handler_info = logging.FileHandler('c:\\Users\\Home\\Desktop\\Python-Automation\\PythonAutomationSample\\src\\tests\\results\\log\\info_log.txt')
		self._handler_warn = logging.FileHandler( os.getcwd() + "/src/tests/results/log/info.txt")
		self._handler_info.setLevel(logging.INFO)
		#create a logging format	
		self._formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		self._handler_warn.setFormatter(self._formatter)
		self._handler_info.setFormatter(self._formatter)
		#add the handler to the logger
		self._logger.addHandler(self._handler_warn)
		self._logger.addHandler(self._handler_info)
		self._logger.info('Information')
		self._logger.warning('Warning')
		

