#!/usr/bin/env bash

source /opt/rh/rh-python36/enable

mkdir /home/vagrant/.virtualenvs
virtualenv --system-site-packages /home/vagrant/.virtualenvs/gpp
source /home/vagrant/.virtualenvs/gpp/bin/activate
pip install -U pip
pip install -U setuptools
pip install -r /vagrant/requirements.txt
