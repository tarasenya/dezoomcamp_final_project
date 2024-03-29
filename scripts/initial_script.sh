#! /bin/bash
apt-get update 
apt-get install -yq git python3 python3-pip python3-distutils 
git clone -b terraform_deployment https://github.com/tarasenya/dezoomcamp_final_project.git 
cd dezoomcamp_final_project
export PYTHONPATH="${PYTHONPATH}:(pwd)"
pip3 install -U pipenv
echo 'export "PATH=~/.local/bin:${PATH}"' >> ~/.bashrc
source ~/.bashrc
pipenv install --deploy
pipenv shell