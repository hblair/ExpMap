#!/usr/bin/env python

from distutils.core import setup
import shutil

setup(name='ExpNameData',
      version='1.0',
      py_modules=['PressedExpData',],
      )

shutil.copyfile("C:\Users\Ian\Desktop\movetest.py", "C:/Users/Ian/Desktop/Project_ExpNameData/Build_Recipie/movetest.py")