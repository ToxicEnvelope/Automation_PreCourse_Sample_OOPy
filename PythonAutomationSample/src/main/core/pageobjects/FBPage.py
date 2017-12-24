#!/usr/bin/env python

from .core.utils.Logger import *

class FBPage(BasePage, object):


	_user_field = find_by(css='input#email.inputtext')
	_pass_field = find_by(css='input#pass.inputtext')
	_login_btn = find_by(css='label > input#loginbutton')


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
				super(BasePage, self).click(login_btn)
				pass
			else:
				super(BasePage, self).snap()
				break
			return True
		except Exception as e:
			super(BasePage, self)._logger.critical("'Invalid Input : " + str(e))
			return False

