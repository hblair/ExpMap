#!/bin/bash

#Change meta.yaml
python AutomatedExpUpload.py

#Commence Building Operation
conda build ExpName

#Initializing Upload to Anaconda.org
anaconda upload Path/to/package/.tar.bz2
