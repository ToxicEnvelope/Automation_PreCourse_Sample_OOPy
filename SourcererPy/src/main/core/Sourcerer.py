#!/usr/bin/env python

import re

class Sourcerer(object):


	def __init__(self, source_code):
		self._source = source_code

	def evaluate_source():
		stack = []
		pushc, popc = "<({[", ">)}]"
		for c in self._source:
			if c in pushc:
				stack.append(c)
			elif c in popc:
				if not len(stack):
					return False
				else:
					stack_top = stack.pop()
					balancing_bracket = pushc[popc.index(c)]
					if stack_top != balancing_bracket:
						return False
			else:
				return False
		return not len(stack)