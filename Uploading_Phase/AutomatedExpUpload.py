# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 17:27:44 2017

@author: Ian
"""
# Automatically updates and uploads packages to the cloud
import os, sys, subprocess, conda
# Search for the package
search = subprocess.check_output(['conda', 'search', 'gladio'])

# Take version number from package
#v = [int(s) for s in search.split() if s.isdigit()]

v = search.split(".")

lastLine = v[len(v)-1]

oldVersionNumber = int(lastLine.split()) 
print oldVersionNumber

newVer = oldVersionNumber[0] + 1
print newVer
'''
jim = len(v)

# Update with new version number
m = jim + 1
print '***New build number is 0.%s***' % m

# Set new commands
pack = 'conda package -p C:\Users\Ian\Anaconda\gladio --pkg-name gladio --pkg-ver 0.%s --pkg-build 0' % m
load = 'anaconda upload gladio-0.%s-0.tar.bz2' % m

# Execute "pack" to create the package
myout = subprocess.check_output(pack.split())
print "***Creating package " + myout

#Execute "load" to upoad it to Anaconda
upout = subprocess.check_output(load.split())
print "***Uploading package " + upout
'''