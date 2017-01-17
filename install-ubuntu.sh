#!/usr/bin/env bash

set -ex
sudo apt-get update
sudo apt-get install -y \
  gfortran \
  libblas-dev \
  libfreetype6-dev \
  liblapack-dev \
  libpng-dev \
  python-dev \
  virtualenv \
;
# --distribute: http://stackoverflow.com/questions/35780537/error-no-module-named-markerlib-when-installing-some-packages-on-virtualenv
virtualenv -p python2.7 .venv --distribute
. .venv/bin/activate
pip install -r requirements.txt

# TODO Last case resort if you can't install something with pip.
#sudo apt-get install -y python-pip
#sudo apt-get install -y python-scipy
#sudo apt-get install -y python-matplotlib
#sudo apt-get install -y python-sip
## Update NumPy version
#sudo pip install -y numpy
