#!/bin/bash
sudo apt update
sudo apt install -y python3 python3-pip
sudo cp tv_grab_italy* /usr/bin/
sudo mv /usr/bin/tv_grab_italy_basic_url.py /usr/bin/tv_grab_italy_basic_url
sudo mv /usr/bin/tv_grab_italy_sky_url.py /usr/bin/tv_grab_italy_sky_url
sudo mv /usr/bin/tv_grab_italy_sport_movies_url.py /usr/bin/tv_grab_italy_sport_movies_url
sudo chmod 777 /usr/bin/tv_grab_italy*
sudo /etc/init.d/tvheadend restart
echo ''
echo 'Dalla WebGUI di TVHeadend accedere al pannello Configuration > Channel > EPG Grabber > EPG Grabber Modules > Selezionare e Attivare i tre Grabber riconoscibili dall'\''etichetta "XMLTV: TV Italy"'