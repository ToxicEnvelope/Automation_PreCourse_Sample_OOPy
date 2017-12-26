#!/usr/bin/env python 


# Setup.py
import os, sys


def load():
	root = os.getcwd()
	pageobjects = '../pageobjects/'
	tests = '../../tests/'
	path = [root, pageobjects, tests]
	for p in path:
		sys.path.insert(0, p)
		print '{} inserted to PYTHONPATH!'.format(str(p))

# # entrypoint.py
# from setup import load
# load()
# # continue with program