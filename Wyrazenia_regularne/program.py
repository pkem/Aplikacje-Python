#! /usr/bin/python
import sys
import os
print sys.path
print sys.argv
print os.curdir

print os.path.exists("program.py")
print os.listdir(".")
print os.environ["USER"]


