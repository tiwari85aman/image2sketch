#!/usr/bin/env bash

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.6
sudo apt-get install python3-pip
sudo pip3 install virtualenv


virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
