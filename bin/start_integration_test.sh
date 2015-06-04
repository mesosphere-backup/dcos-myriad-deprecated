#!/bin/bash

apt-get update
apt-get install python-pip
pip install virtualenv

# Clean and recreate environment
cd /dcos-myriad
make clean env

# Activate the virtual environment so that we can run make
source env/bin/activate

# Run the default target: E.g. test and packages
make
