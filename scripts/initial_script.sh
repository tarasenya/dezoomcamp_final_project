#!/bin/bash
cd /tmp
git clone https://github.com/tarasenya/dezoomcamp_final_project.git
cd dezoomcamp_final_project
pip install -U pip
pip install pipenv
pipenv install --system --deploy
pipenv shell