#!/usr/bin/env python


class FBPage(BasePage, obect):


	def init(self):
		BasePage.__init__(self)

	def attempt_to_authenticate(self, user, passwd):
		try:	
			user_field = super(BasePage, self).wait_until_visible_by_CSS("input#email.inputtext")
			if user_field.is_displayed():
				super(BasePage, self).fill_text(user)
				pass
			else:
				super(BasePage, self).snap()
				break
			pass_field = super(BasePage, self).wait_until_visible_by_CSS("input#pass.inputtext")
			if pass_field.is_displayed():
				super(BasePage, self).fill_text(passwd)
				pass
			else:
				super(BasePage, self).snap()
				break
			login_btn = super(BasePage, self).wait_until_visible_by_CSS("label > input#loginbutton")
			if login_btn.is_displayed():
				super(BasePage, self).click(login_btn)
				pass
			else:
				super(BasePage, self).snap()
				break
			return True
		except Exception as e:
			print str(e)
			return False

