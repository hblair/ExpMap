#!/bin/bash

#Change meta.yaml
python AutoUp.py

#Commence Building Operation
conda build ExpName

#Initializing Upload to Anaconda.org
anaconda upload Path/to/package/.tar.bz2
