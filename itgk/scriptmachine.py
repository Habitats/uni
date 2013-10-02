#! /usr/bin/env python 
# Scriptmachine! :D

import os

scripts = os.listdir('/home/bullshit/python/')
sep = '_____________________________________\n'

def list():
  print sep, "\nThe following scripts are available:\n", sep
  for x in scripts[:]:
     print '  - ', x

def check():
  name = raw_input("\nName of the script you want to run: ")

  if name in scripts:
     print sep, '\nRunning', name, '...\n', sep
     execfile(name)
     return
  if 'list' == name:
     list()
     check()
  else:
     print sep, "\nThere\'s no scripts matching that name!\n", sep
     check()
  return
list()

check()
