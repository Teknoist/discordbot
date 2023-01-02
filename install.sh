#!/bin/bash

#Repoları güncelle
sudo apt-get update
sudo apt-get install

#Gerekli yazılımları yükle
sudo apt-get -y install git python3 python3-pip etherwake

#Github repoyu klonla
sudo git clone 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@github.com:Teknoist/discordbot.git

#Gereklilikleri yükle
python3 -m pip install -r ./discordbot/requirements.txt

sudo rm ./discordbot/requirements.txt
sudo rm ./discordbot/install.sh
