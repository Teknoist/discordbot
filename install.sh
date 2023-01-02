#!/bin/bash

#Repoları güncelle
sudo apt-get update
sudo apt-get install

#Gerekli yazılımları yükle
sudo apt-get -y install git python3 python3-pip etherwake

#Gereklilikleri yükle
python3 -m pip install -r ./requirements.txt
sudo python3 -m pip install -r ./requirements.txt
