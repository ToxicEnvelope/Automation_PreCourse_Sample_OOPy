#!/usr/bin/env python
import os
import sys
try:
	paths = [os.getcwd()]
	for p in paths:
		os.chdir(p)
		current_dir = os.getcwd()
		sys.path.append(current_dir)
	from src.main.core import BasePage
	from src.main.core.utils import Logger
	# online reference -> https://jeremykao.wordpress.com/2015/06/10/pagefactory-pattern-in-python/
	# PageFactory Pattern
	from src.main.core.utils import pageobject_support as ps
except ImportError as e:
	pip = lambda : os.system('pip install' + str(e)[15:])
	pip()

class FBPage(BasePage, object):


	_user_field = ps.find_by(css='input#email.inputtext')
	_pass_field = ps.find_by(css='input#pass.inputtext')
	_login_btn = ps.find_by(css='label > input#loginbutton')


	def init(self):
		BasePage.__init__(self)

	def attempt_to_authenticate(self, user, passwd):
		try:	
			super(BasePage, self).wait_until_visible_by_CSS("input#email.inputtext")
			if self._user_field.is_displayed():
				super(BasePage, self).fill_text(user)
			else:
				super(BasePage, self).snap()
			super(BasePage, self).wait_until_visible_by_CSS("input#pass.inputtext")
			if self._pass_field.is_displayed():
				super(BasePage, self).fill_text(passwd)
			else:
				super(BasePage, self).snap()
			super(BasePage, self).wait_until_visible_by_CSS("label > input#loginbutton")
			if self._login_btn.is_displayed():
				super(BasePage, self).click(self._login_btn)
				pass
			else:
				super(BasePage, self).snap()
			return True
		except Exception as e:
			super(BasePage, self)._logger.critical("'Invalid Input : " + str(e))
			return False

