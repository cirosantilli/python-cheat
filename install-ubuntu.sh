#!/usr/bin/env bash
set -ex
sudo apt-get update
sudo apt-get install -y python-dev virtualenv
# --distribute: http://stackoverflow.com/questions/35780537/error-no-module-named-markerlib-when-installing-some-packages-on-virtualenv
virtualenv -p python2.7 .venv --distribute
. .venv/bin/activate
pip install -r requirements.txt
