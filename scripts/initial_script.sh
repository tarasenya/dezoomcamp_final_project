#!/bin/bash
sudo apt-get update
sudo apt-get install -yq git python3 python-pip python3-distutils
cd /tmp
git clone https://github.com/tarasenya/dezoomcamp_final_project.git
cd dezoomcamp_final_project
pip install pipenv
pipenv install --deploy
pipenv shell