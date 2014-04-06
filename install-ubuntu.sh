#!/usr/bin/env bash

sudo apt-get install -y aptitude

# TODO install with virtualenv
sudo aptitude install -y python-pip

sudo aptitude install -y python-dev
sudo aptitude install -y python-scipy

# For some reason this is really hard to install.
sudo aptitude install -y python-matplotlib
sudo aptitude install -y python-sip
# Update NumPy version
sudo pip install -y numpy

sudo pip install -r requirements.txt
