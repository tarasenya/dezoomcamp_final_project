#! /bin/bash
apt-get update 
apt-get install -yq git python3 python3-pip python3-distutils 
pip3 install pipenv
echo 'export "PATH=~/.local/bin:${PATH}"' >> ~/.bashrc
source ~/.bashrc

