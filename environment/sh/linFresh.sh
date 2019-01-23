#!/bin/bash
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install vim
sudo apt-get install git

sudo apt-get install python-pip
sudo apt-get install python-dev

sudo apt-get install postgres-9.5
sudo apt-get install postgresql-server-dev-9.5




sudo apt-get update
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
sudo apt-get update
sudo apt-get install -y docker-engine
sudo systemctl status docker
sudo usermod -aG docker $(whoami)
sudo apt-get install kazam
sudo apt-get install restview

# para programar en: Python
sudo apt-get install bpython

# para vi
sudo apt-get install libxml2-utils
curl http://j.mp/spf13-vim3 -L -o - | sh

# Software
# google-chrome
# source = https://www.linuxbabe.com/ubuntu/install-google-chrome-ubuntu-16-04-lts
sudo nano /etc/apt/sources.list
deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main
wget https://dl.google.com/linux/linux_signing_key.pub
sudo apt-key add linux_signing_key.pub
sudo apt update
sudo apt install google-chrome-stable

# Telegram
wget https://telegram.org/dl/desktop/linux

#steam (or stemen what ever sound good to you)
http://www.omgubuntu.co.uk/2016/06/install-steam-on-ubuntu-16-04-lts
sudo add-apt-repository multiverse
sudo apt update && sudo apt install steam

# Install travis2docker
sudo pip install  --upgrade git+https://github.com/Vauxoo/travis2docker.git
echo 'alias t2d="travisfile2dockerfile --root-path=${HOME}/.t2d"' >> ~/.bashrc
# This works in 16.04
sudo apt install compizconfig-settings-manager compiz-plugins-extra

# We need this, is to set names to add names to desktops
sudo apt install compiz compizconfig-settings-manager compiz-plugins

#Instalando teamviewer https://vitux.com/how-to-install-teamviewer-on-ubuntu/
cd /tmp
wget https://download.teamviewer.com/download/linux/signature/TeamViewer2017.asc
sudo apt-key add TeamViewer2017.asc
sudo sh -c 'echo "deb http://linux.teamviewer.com/deb stable main" >> /etc/apt/sources.list.d/teamviewer.list'
sudo apt update
sudo apt install teamviewer
