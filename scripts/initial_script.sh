#! /bin/bash
sudo apt-get update 
sudo apt-get install -yq git python3 python3-pip python3-distutils 
cd ~
git clone https://github.com/tarasenya/dezoomcamp_final_project.git 
cd dezoomcamp_final_project
pip3 install pipenv
echo 'export "PATH=~/.local/bin:${PATH}"' >> ~/.bashrc
source ~/.bashrc
pipenv install --deploy
pipenv shell