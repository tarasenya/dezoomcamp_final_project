#!/bin/bash
cd /tmp
git clone https://github.com/tarasenya/dezoomcamp_final_project.git
cd dezoomcamp_final_project
pip install pipenv
pipenv install --deploy
pipenv shell