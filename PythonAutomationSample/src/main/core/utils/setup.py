#!/usr/bin/env python 



# setup.py
import os, sys

def load():
	root = str(os.getcwd())
	pageobjects = '../pageobjects/'
	tests = '../../tests/'
    paths = [root, pageobjects, tests]
    for p in path:
        sys.path.insert(0, p)
        print '{} has inserted to PYTHONPATH'.format(str(p)) 

# entrypoint.py
from setup import load
load()
# continue with program