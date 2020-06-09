#!/bin/bash

sudo add-apt-repository ppa:jonathonf/python-3.6

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install vim
sudo apt-get install git

sudo apt-get install python-pip
sudo apt-get install python-dev

sudo apt-get install postgres-9.5
sudo apt-get install postgresql-server-dev-9.5

# Docker https://linuxconfig.org/how-to-install-docker-on-ubuntu-20-04-lts-focal-fossa
sudo apt-get update
sudo apt install docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $(whoami)

sudo apt-get install kazam
sudo apt-get install restview

# para programar en: Python
sudo apt-get install bpython

# para vi
sudo apt-get install libxml2-utils
curl http://j.mp/spf13-vim3 -L -o - | sh

# Chrome https://linuxconfig.org/how-to-install-google-chrome-web-browser-on-ubuntu-20-04-focal-fossa
sudo apt install gdebi-core wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo gdebi google-chrome-stable_current_amd64.deb

# Telegram
wget https://telegram.org/dl/desktop/linux

# Install travis2docker
sudo pip install  --upgrade git+https://github.com/Vauxoo/travis2docker.git
echo 'alias t2d="travisfile2dockerfile --root-path=${HOME}/.t2d"' >> ~/.bashrc

# Pycharmi https://linuxconfig.org/how-to-install-pycharm-on-ubuntu-20-04-linux-desktop
sudo snap install pycharm-professional --classic
